import ast

from parser_engine.class_builder import ClassBuilder
from parser_engine.function_builder import FunctionBuilder


class ParserVisitor(ast.NodeVisitor):

    def __init__(self):

        self.functions = []
        self.classes = []

        self.function_builder = FunctionBuilder()
        self.class_builder = ClassBuilder()

    # ----------------------------------------
    # Classes
    # ----------------------------------------

    def visit_ClassDef(self, node):

        class_info = self.class_builder.build(node)

        self.classes.append(class_info)

        self.generic_visit(node)

    # ----------------------------------------
    # Normal Functions
    # ----------------------------------------

    def visit_FunctionDef(self, node):

        function = self.function_builder.build(node)

        self.functions.append(function)

        self.generic_visit(node)

    # ----------------------------------------
    # Async Functions
    # ----------------------------------------

    def visit_AsyncFunctionDef(self, node):

        function = self.function_builder.build(node)

        self.functions.append(function)

        self.generic_visit(node)