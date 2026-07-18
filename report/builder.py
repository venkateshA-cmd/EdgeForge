from report.report import EdgeForgeReport


class ReportBuilder:

    def build(
        self,
        analysis,
        findings,
        test_cases,
    ):

        summary = {
            "functions": len(analysis.functions),
            "classes": len(analysis.classes),
            "findings": len(findings),
            "test_cases": len(test_cases),
        }

        return EdgeForgeReport(
            analysis=analysis,
            findings=findings,
            test_cases=test_cases,
            summary=summary,
        )