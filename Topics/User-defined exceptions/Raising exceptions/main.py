class NegativeSumError(Exception):
    def __str__(self):
        return "Negative Sum Exception"


def sum_with_exceptions(a, b):
    if a + b >= 0:
        return a + b
    else:
        raise NegativeSumError