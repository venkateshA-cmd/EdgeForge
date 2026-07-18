import ast

from models.function_info import FunctionInfo
from models.parameter_info import ParameterInfo


class FunctionBuilder:

    def build(self, node: ast.FunctionDef) -> FunctionInfo:

        parameters = []

        defaults = node.args.defaults
        default_start = len(node.args.args) - len(defaults)

        for index, arg in enumerate(node.args.args):

            annotation = None

            if arg.annotation is not None:
                annotation = ast.unparse(arg.annotation)

            default = None

            if index >= default_start:
                default = ast.unparse(
                    defaults[index - default_start]
                )

            parameters.append(
                ParameterInfo(
                    name=arg.arg,
                    annotation=annotation,
                    default=default,
                )
            )

        return_annotation = None

        if node.returns is not None:
            return_annotation = ast.unparse(node.returns)

        return FunctionInfo(
            name=node.name,
            parameters=parameters,
            return_annotation=return_annotation,
            line_number=node.lineno,
            docstring=ast.get_docstring(node),
            body=node.body
        )