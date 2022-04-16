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
import re


class S001_Error(Exception):
    def __init__(self, line_no):
        self.message = f"Line {line_no}: S001 Too long"
        super().__init__(self.message)


class S002_Error(Exception):
    def __init__(self, line_no):
        self.message = f"Line {line_no}: S002 Indentation is not a multiple of four"
        super().__init__(self.message)


class S003_Error(Exception):
    def __init__(self, line_no):
        self.message = f"Line {line_no}: S003 Unnecessary semicolon after a statement"
        super().__init__(self.message)


class S004_Error(Exception):
    def __init__(self, line_no):
        self.message = f"Line {line_no}: S004 Less than two spaces before inline comments"
        super().__init__(self.message)


class S005_Error(Exception):
    def __init__(self, line_no):
        self.message = f"Line {line_no}: S005  TODO found in comments"
        super().__init__(self.message)


class S006_Error(Exception):
    def __init__(self, line_no):
        self.message = f"Line {line_no}: S006  More than two blank lines preceding a code line"
        super().__init__(self.message)


def check_len(num, line):
    if len(line) > 79:
        raise S001_Error(num)


def check_indent(num, line):
    space_count = 0
    if re.search(r'[^\s]', line):
        space_count = re.search(r'[^\s]', line).start()
    if space_count % 4 != 0:
        raise S002_Error(num)


def check_semicolon(num, line):
    line = line.rstrip()
    if re.search(r';$', line):
        raise S003_Error(num)


def check_space_before_comments(num, line, comment):
    if comment and line and not re.search(r'\s{2,}$', line):
        raise S004_Error(num)


def check_TODO_in_comments(num, line):
    if re.search(r'TODO', line, flags=re.IGNORECASE):
        raise S005_Error(num)


def check_blank_lines(num, count):
    if count > 2:
        raise S006_Error(num)


if __name__ == "__main__":
    file_name = input()
    with open(file_name, 'r') as reader:
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
                empty_lines = 0




