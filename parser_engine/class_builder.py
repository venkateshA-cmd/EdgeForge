import ast

from models.class_info import ClassInfo
from parser_engine.function_builder import FunctionBuilder


class ClassBuilder:
    """
    Responsible for converting an AST ClassDef
    into a ClassInfo object.
    """

    def __init__(self):

        self.function_builder = FunctionBuilder()

    def build(self, node: ast.ClassDef) -> ClassInfo:

        methods = []

        for item in node.body:

            if isinstance(item, ast.FunctionDef):
                methods.append(
                    self.function_builder.build(item)
                )

        bases = []

        for base in node.bases:
            bases.append(ast.unparse(base))

        return ClassInfo(
            name=node.name,
            methods=methods,
            bases=bases,
            line_number=node.lineno,
            docstring=ast.get_docstring(node),
        )