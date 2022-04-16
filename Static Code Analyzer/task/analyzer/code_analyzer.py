# ------------------------------------------------------- STAGE 1-------------------------------------------------------
# class S001_Error(Exception):
#     def __init__(self, line_no):
#         self.message = f"Line {line_no}: S001 Too long"
#         super().__init__(self.message)
#
#
# def check_len(_num, _line):
#     if len(_line) > 79:
#         raise S001_Error(_num)
#
#
# if __name__ == "__main__":
#     file_name = input()
#     with open(file_name, 'r') as reader:
#         # check for S001 error
#         for num, line in enumerate(reader.readlines()):
#             try:
#                 check_len(num + 1, line)
#             except S001_Error as s01_err:
#                 print(s01_err)

# ------------------------------------------------------- STAGE 2-------------------------------------------------------
# import re
#
#
# class S001_Error(Exception):
#     def __init__(self, line_no):
#         self.message = f"Line {line_no}: S001 Too long"
#         super().__init__(self.message)
#
#
# class S002_Error(Exception):
#     def __init__(self, line_no):
#         self.message = f"Line {line_no}: S002 Indentation is not a multiple of four"
#         super().__init__(self.message)
#
#
# class S003_Error(Exception):
#     def __init__(self, line_no):
#         self.message = f"Line {line_no}: S003 Unnecessary semicolon after a statement"
#         super().__init__(self.message)
#
#
# class S004_Error(Exception):
#     def __init__(self, line_no):
#         self.message = f"Line {line_no}: S004 Less than two spaces before inline comments"
#         super().__init__(self.message)
#
#
# class S005_Error(Exception):
#     def __init__(self, line_no):
#         self.message = f"Line {line_no}: S005  TODO found in comments"
#         super().__init__(self.message)
#
#
# class S006_Error(Exception):
#     def __init__(self, line_no):
#         self.message = f"Line {line_no}: S006  More than two blank lines preceding a code line"
#         super().__init__(self.message)
#
#
# def check_len(num, line):
#     if len(line) > 79:
#         raise S001_Error(num)
#
#
# def check_indent(num, line):
#     space_count = 0
#     if re.search(r'[^\s]', line):
#         space_count = re.search(r'[^\s]', line).start()
#     if space_count % 4 != 0:
#         raise S002_Error(num)
#
#
# def check_semicolon(num, line):
#     line = line.rstrip()
#     if re.search(r';$', line):
#         raise S003_Error(num)
#
#
# def check_space_before_comments(num, line, comment):
#     if comment and line and not re.search(r'\s{2,}$', line):
#         raise S004_Error(num)
#
#
# def check_TODO_in_comments(num, line):
#     if re.search(r'TODO', line, flags=re.IGNORECASE):
#         raise S005_Error(num)
#
#
# def check_blank_lines(num, count):
#     if count > 2:
#         raise S006_Error(num)
#
#
# if __name__ == "__main__":
#     file_name = input()
#     with open(file_name, 'r') as reader:
#         empty_lines = 0
#         for num, line in enumerate(reader.readlines()):
#             line = line[:-1]
#             if not line:
#                 empty_lines += 1
#             else:
#                 if re.match(r'[^\#]*', line):
#                     code = re.match(r'[^\u0023]*', line).group()
#                     # code = re.sub(r"'.*?'","",code)
#                     # code = re.sub(r'".*?"', '', code)
#                 if re.search(r'\u0023.*', line, flags=re.DOTALL):
#                     comment = re.search(r'\u0023.*', line, flags=re.DOTALL).group()
#                 else:
#                     comment = ''
#                 # print("_________", num, "code:", code, "comment:", comment)
#                 try:                                                    # check S001 - line length
#                     check_len(num + 1, line)
#                 except S001_Error as s01_err:
#                     print(s01_err)
#                 try:                                                    # check S002 - indention
#                     check_indent(num + 1, code)
#                 except S002_Error as s02_err:
#                     print(s02_err)
#                 try:                                                    # check S003 - semicolon
#                     check_semicolon(num + 1, code)
#                 except S003_Error as s03_err:
#                     print(s03_err)
#                 try:                                                    # check S004 - spaces before comments
#                     check_space_before_comments(num + 1, code, comment)
#                 except S004_Error as s04_err:
#                     print(s04_err)
#                 try:                                                    # check S005 - TODO in comments
#                     check_TODO_in_comments(num + 1, comment)
#                 except S005_Error as s05_err:
#                     print(s05_err)
#                 try:                                                    # check S006 - blank lines
#                     check_blank_lines(num + 1, empty_lines)
#                 except S006_Error as s06_err:
#                     print(s06_err)
#                 empty_lines = 0

# ------------------------------------------------------- STAGE 3-------------------------------------------------------
# import re
# import sys
# import os
#
#
# class S001_Error(Exception):
#     def __init__(self, full_file_name, line_no):
#         self.message = f"{full_file_name}: Line {line_no}: S001 Too long"
#         super().__init__(self.message)
#
#
# class S002_Error(Exception):
#     def __init__(self, full_file_name, line_no):
#         self.message = f"{full_file_name}: Line {line_no}: S002 Indentation is not a multiple of four"
#         super().__init__(self.message)
#
#
# class S003_Error(Exception):
#     def __init__(self, full_file_name, line_no):
#         self.message = f"{full_file_name}: Line {line_no}: S003 Unnecessary semicolon after a statement"
#         super().__init__(self.message)
#
#
# class S004_Error(Exception):
#     def __init__(self, full_file_name, line_no):
#         self.message = f"{full_file_name}: Line {line_no}: S004 Less than two spaces before inline comments"
#         super().__init__(self.message)
#
#
# class S005_Error(Exception):
#     def __init__(self, full_file_name, line_no):
#         self.message = f"{full_file_name}: Line {line_no}: S005  TODO found in comments"
#         super().__init__(self.message)
#
#
# class S006_Error(Exception):
#     def __init__(self, full_file_name, line_no):
#         self.message = f"{full_file_name}: Line {line_no}: S006  More than two blank lines preceding a code line"
#         super().__init__(self.message)
#
#
# def check_len(num, line):
#     if len(line) > 79:
#         raise S001_Error(dir + file_name, num)
#
#
# def check_indent(num, line):
#     space_count = 0
#     if re.search(r'[^\s]', line):
#         space_count = re.search(r'[^\s]', line).start()
#     if space_count % 4 != 0:
#         raise S002_Error(dir + file_name, num)
#
#
# def check_semicolon(num, line):
#     line = line.rstrip()
#     if re.search(r';$', line):
#         raise S003_Error(dir + file_name, num)
#
#
# def check_space_before_comments(num, line, comment):
#     if comment and line and not re.search(r'\s{2,}$', line):
#         raise S004_Error(dir + file_name, num)
#
#
# def check_TODO_in_comments(num, line):
#     if re.search(r'TODO', line, flags=re.IGNORECASE):
#         raise S005_Error(dir + file_name, num)
#
#
# def check_blank_lines(num, count):
#     if count > 2:
#         raise S006_Error(dir + file_name, num)
#
#
# if __name__ == "__main__":
#     args = sys.argv
#     files_py = []
#     #  check if program attribute is python file
#     if re.search(r'\.py', args[1]):
#         files_py.append(args[1])
#         dir = ''
#     elif not re.search(r'\.', args[1]):
#         dir = args[1] + '/'
#         for file in os.listdir(dir):
#             if re.search(r'\.py', str(file)):
#                 files_py.append(file)
#         # os.chdir(dir)
#
#     for file_name in sorted(files_py):
#         with open(dir + file_name, 'r') as reader:
#             empty_lines = 0
#             for num, line in enumerate(reader.readlines()):
#                 line = line[:-1]
#                 if not line:
#                     empty_lines += 1
#                 else:
#                     if re.match(r'[^\#]*', line):
#                         code = re.match(r'[^\u0023]*', line).group()
#                         # code = re.sub(r"'.*?'","",code)
#                         # code = re.sub(r'".*?"', '', code)
#                     if re.search(r'\u0023.*', line, flags=re.DOTALL):
#                         comment = re.search(r'\u0023.*', line, flags=re.DOTALL).group()
#                     else:
#                         comment = ''
#                     # print("_________", num, "code:", code, "comment:", comment)
#                     try:                                                    # check S001 - line length
#                         check_len(num + 1, line)
#                     except S001_Error as s01_err:
#                         print(s01_err)
#                     try:                                                    # check S002 - indention
#                         check_indent(num + 1, code)
#                     except S002_Error as s02_err:
#                         print(s02_err)
#                     try:                                                    # check S003 - semicolon
#                         check_semicolon(num + 1, code)
#                     except S003_Error as s03_err:
#                         print(s03_err)
#                     try:                                                    # check S004 - spaces before comments
#                         check_space_before_comments(num + 1, code, comment)
#                     except S004_Error as s04_err:
#                         print(s04_err)
#                     try:                                                    # check S005 - TODO in comments
#                         check_TODO_in_comments(num + 1, comment)
#                     except S005_Error as s05_err:
#                         print(s05_err)
#                     try:                                                    # check S006 - blank lines
#                         check_blank_lines(num + 1, empty_lines)
#                     except S006_Error as s06_err:
#                         print(s06_err)
#                     empty_lines = 0

# ------------------------------------------------------- STAGE 4-------------------------------------------------------
import re
import sys
import os


class S001_Error(Exception):
    def __init__(self, full_file_name, line_no):
        self.message = f"{full_file_name}: Line {line_no}: S001 Too long"
        super().__init__(self.message)


class S002_Error(Exception):
    def __init__(self, full_file_name, line_no):
        self.message = f"{full_file_name}: Line {line_no}: S002 Indentation is not a multiple of four"
        super().__init__(self.message)


class S003_Error(Exception):
    def __init__(self, full_file_name, line_no):
        self.message = f"{full_file_name}: Line {line_no}: S003 Unnecessary semicolon after a statement"
        super().__init__(self.message)


class S004_Error(Exception):
    def __init__(self, full_file_name, line_no):
        self.message = f"{full_file_name}: Line {line_no}: S004 Less than two spaces before inline comments"
        super().__init__(self.message)


class S005_Error(Exception):
    def __init__(self, full_file_name, line_no):
        self.message = f"{full_file_name}: Line {line_no}: S005  TODO found in comments"
        super().__init__(self.message)


class S006_Error(Exception):
    def __init__(self, full_file_name, line_no):
        self.message = f"{full_file_name}: Line {line_no}: S006  More than two blank lines preceding a code line"
        super().__init__(self.message)


class S007_Error(Exception):
    def __init__(self, full_file_name, line_no):
        self.message = f"{full_file_name}: Line {line_no}: S007  Too many spaces after def/class"
        super().__init__(self.message)


class S008_Error(Exception):
    def __init__(self, full_file_name, line_no):
        self.message = f"{full_file_name}: Line {line_no}: S008  Class name should be in CamelCase"
        super().__init__(self.message)


class S009_Error(Exception):
    def __init__(self, full_file_name, line_no):
        self.message = f"{full_file_name}: Line {line_no}: S009  Function name should be in snake_case"
        super().__init__(self.message)


def check_len(num, line):
    if len(line) > 79:
        raise S001_Error(dir + file_name, num)


def check_indent(num, line):
    space_count = 0
    if re.search(r'[^\s]', line):
        space_count = re.search(r'[^\s]', line).start()
    if space_count % 4 != 0:
        raise S002_Error(dir + file_name, num)


def check_semicolon(num, line):
    line = line.rstrip()
    if re.search(r';$', line):
        raise S003_Error(dir + file_name, num)


def check_space_before_comments(num, line, comment):
    if comment and line and not re.search(r'\s{2,}$', line):
        raise S004_Error(dir + file_name, num)


def check_TODO_in_comments(num, line):
    if re.search(r'TODO', line, flags=re.IGNORECASE):
        raise S005_Error(dir + file_name, num)


def check_blank_lines(num, count):
    if count > 2:
        raise S006_Error(dir + file_name, num)


def check_spaces_before_class_or_func(num, line):
    if re.search(r'(class|def)(?=\s{2,})', line):
        raise S007_Error(dir + file_name, num)


def check_class_name(num, line):
    if re.search(r'class', line) and not re.search(r'(?<=class)\s*([A-Z][a-z]+)+[:(]([A-Z][a-z]+\)+)?', line):
        raise S008_Error(dir + file_name, num)


def check_func_name(num, line):
    if re.search(r'def', line) and not re.search(r'(?<=def)\s*[a-z_][a-z_0-9]*', line):
        raise S009_Error(dir + file_name, num)


if __name__ == "__main__":
    args = sys.argv
    files_py = []
    #  check if program attribute is python file
    if re.search(r'\.py', args[1]):
        files_py.append(args[1])
        dir = ''
    elif not re.search(r'\.', args[1]):
        dir = args[1] + '/'
        for file in os.listdir(dir):
            if re.search(r'\.py', str(file)):
                files_py.append(file)
        # os.chdir(dir)

    for file_name in sorted(files_py):
        with open(dir + file_name, 'r') as reader:
            empty_lines = 0
            for num, line in enumerate(reader.readlines()):
                line = line[:-1]
                if not line:
                    empty_lines += 1
                else:
                    if re.match(r'[^\#]*', line):
                        code = re.match(r'[^\u0023]*', line).group()
                        # code = re.sub(r"'.*?'","",code)
                        # code = re.sub(r'".*?"', '', code)
                    if re.search(r'\u0023.*', line, flags=re.DOTALL):
                        comment = re.search(r'\u0023.*', line, flags=re.DOTALL).group()
                    else:
                        comment = ''
                    # print("_________", num, "code:", code, "comment:", comment)
                    try:                                                    # check S001 - line length
                        check_len(num + 1, line)
                    except S001_Error as s01_err:
                        print(s01_err)
                    try:                                                    # check S002 - indention
                        check_indent(num + 1, code)
                    except S002_Error as s02_err:
                        print(s02_err)
                    try:                                                    # check S003 - semicolon
                        check_semicolon(num + 1, code)
                    except S003_Error as s03_err:
                        print(s03_err)
                    try:                                                    # check S004 - spaces before comments
                        check_space_before_comments(num + 1, code, comment)
                    except S004_Error as s04_err:
                        print(s04_err)
                    try:                                                    # check S005 - TODO in comments
                        check_TODO_in_comments(num + 1, comment)
                    except S005_Error as s05_err:
                        print(s05_err)
                    try:                                                    # check S006 - blank lines
                        check_blank_lines(num + 1, empty_lines)
                    except S006_Error as s06_err:
                        print(s06_err)
                    try:                                                    # check S007 - spaces after def/clas
                        check_spaces_before_class_or_func(num + 1, code)
                    except S007_Error as s07_err:
                        print(s07_err)
                    try:                                                    # check S008 - class name
                        check_class_name(num + 1, code)
                    except S008_Error as s08_err:
                        print(s08_err)
                    try:                                                    # check S009 - function name
                        check_func_name(num + 1, code)
                    except S009_Error as s09_err:
                        print(s09_err)
                    empty_lines = 0

