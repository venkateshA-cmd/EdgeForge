import argparse
from pathlib import Path

from analyzer.analyzer import Analyzer
from generator.generator import EdgeCaseGenerator
from parser_engine.parser import PythonParser
from report.builder import ReportBuilder
from report.html_generator import HTMLReportGenerator


def analyze_file(file_path: str):

    path = Path(file_path)

    if not path.exists():

        print(f"Error: File not found -> {file_path}")
        return

    source_code = path.read_text(encoding="utf-8")

    print("=" * 60)
    print("EDGEFORGE")
    print("=" * 60)

    print("✔ Parsing file...")

    parser = PythonParser()
    analysis = parser.parse(source_code)

    print("✔ Running analyzer...")

    analyzer = Analyzer()
    findings = analyzer.analyze(analysis)

    print("✔ Generating edge cases...")

    generator = EdgeCaseGenerator()
    test_cases = generator.generate(analysis)

    print("✔ Building report...")

    builder = ReportBuilder()

    report = builder.build(
        analysis,
        findings,
        test_cases,
    )

    html = HTMLReportGenerator()

    output = html.generate(report)

    print("✔ HTML Report Created")

    print()
    print("Saved to:")
    print(output)


def main():

    parser = argparse.ArgumentParser(
        prog="EdgeForge",
        description="AI Software Verification Platform"
    )

    subparser = parser.add_subparsers(dest="command")

    analyze = subparser.add_parser(
        "analyze",
        help="Analyze a Python file"
    )

    analyze.add_argument(
        "file",
        help="Python file to analyze"
    )

    args = parser.parse_args()

    if args.command == "analyze":
        analyze_file(args.file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()