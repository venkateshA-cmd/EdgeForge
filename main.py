from analyzer.analyzer import Analyzer
from generator.generator import EdgeCaseGenerator
from parser_engine.parser import PythonParser
from report.builder import ReportBuilder
from report.html_generator import HTMLReportGenerator

source_code = """
def divide(a, b):
    return a / b

def login(username, password):
    return True
"""

# Parse

parser = PythonParser()

analysis = parser.parse(source_code)

# Analyze

analyzer = Analyzer()

findings = analyzer.analyze(analysis)

# Generate Test Cases

generator = EdgeCaseGenerator()

test_cases = generator.generate(analysis)

# Build Report

builder = ReportBuilder()

report = builder.build(
    analysis,
    findings,
    test_cases
)

# Generate HTML

html = HTMLReportGenerator()

path = html.generate(report)

print("=" * 70)
print("EDGEFORGE MVP")
print("=" * 70)

print()

print("HTML Report Generated Successfully!")

print(f"Location : {path}")