class WordError(Exception):
    def __str__(self):
        print("w not allowed to be in word")


def check_w_letter(word):
    if 'w' in word:
        raise WordError
    else:
        return word
