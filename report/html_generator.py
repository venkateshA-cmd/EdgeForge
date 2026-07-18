from pathlib import Path


class HTMLReportGenerator:
    """
    Generates a simple HTML report.
    """

    def generate(self, report):

        html = f"""
<!DOCTYPE html>

<html>

<head>

<title>EdgeForge Report</title>

<style>

body {{

font-family: Arial;

margin:40px;

background:#f5f5f5;

}}

.card {{

background:white;

padding:20px;

margin-bottom:20px;

border-radius:8px;

box-shadow:0px 0px 8px rgba(0,0,0,.1);

}}

table {{

width:100%;

border-collapse:collapse;

}}

th,td {{

border:1px solid #ddd;

padding:10px;

}}

th {{

background:#333;

color:white;

}}

</style>

</head>

<body>

<h1>EdgeForge Analysis Report</h1>

<div class="card">

<h2>Summary</h2>

<p><b>Functions:</b> {report.summary["functions"]}</p>

<p><b>Classes:</b> {report.summary["classes"]}</p>

<p><b>Findings:</b> {report.summary["findings"]}</p>

<p><b>Generated Tests:</b> {report.summary["test_cases"]}</p>

</div>

<div class="card">

<h2>Findings</h2>

<table>

<tr>

<th>Severity</th>

<th>Function</th>

<th>Issue</th>

</tr>
"""

        for finding in report.findings:

            html += f"""

<tr>

<td>{finding.severity}</td>

<td>{finding.function_name}</td>

<td>{finding.title}</td>

</tr>

"""

        html += """

</table>

</div>

<div class="card">

<h2>Generated Test Cases</h2>

<table>

<tr>

<th>Function</th>

<th>Inputs</th>

<th>Reason</th>

</tr>

"""

        for test in report.test_cases:

            html += f"""

<tr>

<td>{test.function_name}</td>

<td>{tuple(test.inputs)}</td>

<td>{test.reason}</td>

</tr>

"""

        html += """

</table>

</div>

</body>

</html>

"""

        output_folder = Path("report/output")

        output_folder.mkdir(exist_ok=True)

        output_file = output_folder / "report.html"

        output_file.write_text(
            html,
            encoding="utf-8"
        )

        return output_file