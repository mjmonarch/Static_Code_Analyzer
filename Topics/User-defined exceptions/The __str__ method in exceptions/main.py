def check_integer(num):
    if num in range(45, 67):
        return num
    else:
        raise NotInBoundsError

def error_handling(num):
    try:
        print(check_integer(num))
    except NotInBoundsError as err:
        print(err)
