# ------------------------------------------------------- STAGE 1-------------------------------------------------------
class S001_Error(Exception):
    def __init__(self, line_no):
        self.message = f"Line {line_no}: S001 Too long"
        super().__init__(self.message)


def check_len(_num, _line):
    if len(_line) > 79:
        raise S001_Error(_num)


if __name__ == "__main__":
    file_name = input()
    with open(file_name, 'r') as reader:
        # check forS S001 error
        for num, line in enumerate(reader.readlines()):
            try:
                check_len(num + 1, line)
            except S001_Error as s01_err:
                print(s01_err)



