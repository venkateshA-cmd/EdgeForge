from pathlib import Path

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
)

from analyzer.analyzer import Analyzer
from generator.generator import EdgeCaseGenerator
from parser_engine.parser import PythonParser
from report.builder import ReportBuilder
from report.html_generator import HTMLReportGenerator


# ==========================================================
# Flask Configuration
# ==========================================================

app = Flask(__name__)

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

REPORT_FOLDER = Path("report/output")
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)


# ==========================================================
# Helper Functions
# ==========================================================

def calculate_risk(findings: int) -> str:
    """
    Calculate risk level based on findings count.
    """

    if findings == 0:
        return "LOW"

    if findings <= 3:
        return "MEDIUM"

    return "HIGH"


def empty_dashboard(filename: str):
    """
    Dashboard returned for empty Python files.
    """

    return render_template(
        "result.html",
        summary={
            "functions": 0,
            "classes": 0,
            "findings": 0,
            "test_cases": 0,
        },
        findings=[],
        test_cases=[],
        report_location="No report generated.",
        filename=filename,
        risk="LOW",
        empty_file=True,
    )


# ==========================================================
# Home
# ==========================================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================================
# Analyze
# ==========================================================

@app.route("/analyze", methods=["POST"])
def analyze():

    # ----------------------------------------
    # Validate Upload
    # ----------------------------------------

    if "file" not in request.files:
        return redirect(url_for("home"))

    uploaded_file = request.files["file"]

    if uploaded_file.filename == "":
        return redirect(url_for("home"))

    if not uploaded_file.filename.lower().endswith(".py"):

        return render_template(
            "index.html",
            error="Please upload a valid Python (.py) file."
        )

    # ----------------------------------------
    # Save Upload
    # ----------------------------------------

    save_path = UPLOAD_FOLDER / uploaded_file.filename

    uploaded_file.save(save_path)

    # ----------------------------------------
    # Read File
    # ----------------------------------------

    try:

        source_code = save_path.read_text(
            encoding="utf-8"
        )

    except Exception:

        return render_template(
            "index.html",
            error="Unable to read uploaded file."
        )

    # ----------------------------------------
    # Empty File
    # ----------------------------------------

    if not source_code.strip():
        return empty_dashboard(uploaded_file.filename)

    # ----------------------------------------
    # Parse Python Source
    # ----------------------------------------

    parser = PythonParser()

    try:

        analysis = parser.parse(source_code)
        
        # ----------------------------------------
# Parser Error Check
# ----------------------------------------

        if analysis.errors:

            return render_template(

            "index.html",

            error=analysis.errors[0]

    )

    except Exception as e:

        return render_template(
            "index.html",
            error=f"Parser Error : {e}"
        )

    # ----------------------------------------
    # Static Analysis
    # ----------------------------------------

    analyzer = Analyzer()

    try:

        findings = analyzer.analyze(
            analysis
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=f"Analyzer Error : {e}"
        )

    # ----------------------------------------
    # Edge Case Generation
    # ----------------------------------------

    generator = EdgeCaseGenerator()

    try:

        test_cases = generator.generate(
            analysis
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=f"Generator Error : {e}"
        )

    # ----------------------------------------
    # Build Report
    # ----------------------------------------

    builder = ReportBuilder()

    report = builder.build(
        analysis,
        findings,
        test_cases,
    )
    
        # ----------------------------------------
    # Generate HTML Report
    # ----------------------------------------

    try:

        html_generator = HTMLReportGenerator()

        report_path = html_generator.generate(report)

    except Exception:

        report_path = REPORT_FOLDER / "report.html"

    # ----------------------------------------
    # Risk Level
    # ----------------------------------------

    risk = calculate_risk(
        report.summary["findings"]
    )

    # ----------------------------------------
    # Render Dashboard
    # ----------------------------------------

    return render_template(

        "result.html",

        summary=report.summary,

        findings=report.findings,

        test_cases=report.test_cases,

        report_location=str(report_path),

        filename=uploaded_file.filename,

        risk=risk,

        empty_file=False,

    )


# ==========================================================
# Download HTML Report
# ==========================================================

@app.route("/download-report")
def download_report():

    report_path = REPORT_FOLDER / "report.html"

    if not report_path.exists():

        return render_template(

            "index.html",

            error="Report not found. Please analyze a file first."

        )

    return send_file(

        report_path,

        as_attachment=True,

        download_name="EdgeForge_Report.html",

        mimetype="text/html"

    )


# ==========================================================
# Error Pages
# ==========================================================

@app.errorhandler(404)
def page_not_found(error):

    return (

        render_template(

            "index.html",

            error="Requested page was not found."

        ),

        404,

    )


@app.errorhandler(500)
def internal_server_error(error):

    return (

        render_template(

            "index.html",

            error="Unexpected internal server error."

        ),

        500,

    )


# ==========================================================
# Run Application
# ==========================================================

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )