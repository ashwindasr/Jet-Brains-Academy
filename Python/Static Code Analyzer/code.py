import os
import re
import sys
import ast
from pprint import pprint


class FunctionAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"def": []}

    def visit_FunctionDef(self, node):
        self.stats["def"].append(node)
        self.generic_visit(node)

    def report(self):
        return self.stats


class VariableAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"var": []}

    def visit_Name(self, node):
        self.stats["var"].append(node)
        self.generic_visit(node)

    def report(self):
        return self.stats


class CodeAnalyzer:
    def __init__(self, path):
        self.path = path
        self.base_path = path

    # [S001] Too long
    def check_length(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                if len(line.strip()) > 79:
                    local_errors.append(f"Line {line_no}: S001 Too long")
        return local_errors

    # [S002] Indentation is not a multiple of four
    def check_indentation(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip("\n")
                spaces = re.findall(r"^( +)", line)
                if spaces:
                    if len(spaces[0]) % 4 != 0:
                        local_errors.append(f"Line {line_no}: S002 Indentation is not a multiple of four")
        return local_errors

    # [S003] Unnecessary semicolon after a statement
    def check_semicolon(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                flag = False
                line = line.strip()
                if "#" in line:
                    if re.match(r".+; *#.*", line):
                        flag = True
                else:
                    if re.findall(r";$", line):
                        flag = True
                if flag:
                    local_errors.append(f"Line {line_no}: S003 Unnecessary semicolon after a statement")
        return local_errors

    # [S004] At least two spaces before inline comments required
    def check_inline_comment_spaces(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip()
                if "#" in line:
                    spaces = re.findall(r"( *)#.*", line)[0]
                    if len(spaces) < 2 and not re.match(r"^ *#", line):
                        local_errors.append(
                            f"Line {line_no}: S004 At least two spaces before inline comments required")
        return local_errors

    # [S005] TODO found
    def check_todo(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip()
                if "# todo" in line.lower():
                    local_errors.append(f"Line {line_no}: S005 TODO found")
        return local_errors

    # [S006] More than two blank lines used before this line
    def check_blank_lines(self):
        local_errors = []
        with open(self.path) as file:
            code = file.readlines()
            counter = 0
            for line_no, line in enumerate(code, 1):
                if line == "\n":
                    counter += 1
                else:
                    if counter > 2:
                        local_errors.append(f"Line {line_no}: S006 More than two blank lines used before this line")
                    counter = 0
        return local_errors

    # [S007] Too many spaces after '%construction_name%' (def or class)
    def check_construction_spaces(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip()
                if "class" in line or "def" in line:
                    if "class" in line:
                        category = "class"
                        spaces = re.findall(r" *class( +)\w+:", line)
                    else:
                        category = "def"
                        spaces = re.findall(r" *def( +)\w+\(.*\):", line)

                    if spaces and len(spaces[0]) > 1:
                        local_errors.append(f"Line {line_no}: S007 Too many spaces after '{category}'")
        return local_errors

    # [S008] Class name '%class_name%' should use CamelCase
    def check_camel_case(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip()
                if "class" in line:
                    class_name = re.findall(r" *class *(\w+):", line)
                    if class_name and not class_name[0][0].isupper():
                        local_errors.append(f"Line {line_no}: S008 Class name '{class_name[0]}' should use CamelCase")
        return local_errors

    # [S009] Function name '%function_name%' should use snake_case
    def check_snake_case(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip()
                if "def" in line:
                    line = line.strip()
                    function_name = re.findall(r" *def *(\w+)\(.*\):", line)
                    if function_name and any(x.isupper() for x in function_name[0]):
                        local_errors.append(
                            f"Line {line_no}: S009 Function name '{function_name[0]}' should use snake_case")
        return local_errors

    # [S010] Argument name '%arg_name%' should be snake_case
    def check_arg_snake_case(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip()
                if "def" in line:
                    parameter = re.findall(r" *def *\w+\((.*)\):", line)
                    if parameter:
                        parameters = parameter[0].split(",")
                        parameters = [x.strip() for x in parameters]
                        for to_check in parameters:
                            if "=" in to_check:
                                argument_name = to_check.split("=")[0]
                                if any(x.isupper() for x in argument_name):
                                    local_errors.append(
                                        f"Line {line_no}: S010 Argument name '{argument_name}' should be snake_case")
                            else:
                                argument_name = to_check
                                if any(x.isupper() for x in argument_name):
                                    local_errors.append(
                                        f"Line {line_no}: S010 Argument name '{argument_name}' should be snake_case")
        return local_errors

    # [S012] Default argument value is mutable
    def check_default_arg_mutability(self):
        local_errors = []
        with open(self.path) as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip()
                if "def" in line:
                    parameter = re.findall(r" *def *\w+\((.*)\):", line)
                    if parameter:
                        parameters = parameter[0].split(",")
                        parameters = [x.strip() for x in parameters]
                        for to_check in parameters:
                            if "=" in to_check:
                                parameter_value = to_check.split("=")[1]
                                if len(parameter_value) == 2 and any(x in parameter_value for x in ["[]", "{}", "()"]):
                                    local_errors.append(f"Line {line_no}: S012 Default argument value is mutable")
        return local_errors

    def check_function_variables(self):
        local_errors = []
        with open(self.path, "r") as source:
            try:
                tree = ast.parse(source.read())
            except:
                return []

        func_analyzer = FunctionAnalyzer()
        func_analyzer.visit(tree)
        nodes = func_analyzer.report()['def']
        for node in nodes:
            var_analyzer = VariableAnalyzer()
            var_analyzer.visit(node)
            data = var_analyzer.report()["var"]

            flag = False
            for variable in data:
                if variable.id == "print":
                    flag = True
                if any(x.isupper() for x in variable.id):
                    if flag:
                        flag = False
                        continue
                    local_errors.append(
                        f"Line {variable.lineno}: S011 Variable '{variable.id}' in function should be snake_case")
        return local_errors

    def check_if_file(self):
        return os.path.isfile(self.path)

    def file_check_all(self):
        all_errors = []

        all_errors += self.check_length()
        all_errors += self.check_indentation()
        all_errors += self.check_semicolon()
        all_errors += self.check_inline_comment_spaces()
        all_errors += self.check_todo()
        all_errors += self.check_blank_lines()
        all_errors += self.check_construction_spaces()
        all_errors += self.check_camel_case()
        all_errors += self.check_snake_case()
        all_errors += self.check_arg_snake_case()
        all_errors += self.check_default_arg_mutability()
        all_errors += self.check_function_variables()

        return sorted(all_errors, key=lambda x: int(x.split()[1][:-1]))

    def all_files_check(self):
        all_files_errors = {}
        files = sorted(os.listdir(self.path))
        for file in files:
            if re.match(r".*\.py$", file):
                self.path = self.base_path + f"/{file}"
                all_files_errors[f"{self.base_path}/{file}"] = self.file_check_all()

        return all_files_errors


def main():
    analyzer = CodeAnalyzer(sys.argv[1])
    if analyzer.check_if_file():
        errors = analyzer.file_check_all()
        for data in errors:
            print(f"{analyzer.path}: {data}")
    else:
        errors = analyzer.all_files_check()
        for error in errors:
            for data in errors[error]:
                print(f"{error}: {data}")


if __name__ == '__main__':
    main()
