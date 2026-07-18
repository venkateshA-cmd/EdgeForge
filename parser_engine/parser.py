import ast

from models.analysis_result import AnalysisResult
from parser_engine.visitor import ParserVisitor


class PythonParser:

    def parse(self, source_code: str) -> AnalysisResult:

        result = AnalysisResult()

        try:
            tree = ast.parse(source_code)

        except SyntaxError as error:

            result.errors.append(
                f"Syntax Error at line {error.lineno}: {error.msg}"
            )

            return result

        # ---------------------------------
        # Add parent references
        # ---------------------------------

        for parent in ast.walk(tree):

            for child in ast.iter_child_nodes(parent):
                child.parent = parent

        visitor = ParserVisitor()

        visitor.visit(tree)

        result.functions = visitor.functions
        result.classes = visitor.classes

        return result