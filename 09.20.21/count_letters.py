import string


def count_letters(text):
    d = dict()
    for ch in string.ascii_letters:
        d[ch] = text.count(ch)
    return d


def dict_string(string):
    dictionary = dict()
    seen = ""
    for char in string:
        if char not in seen:
            dictionary[char] = string.count(char)
            seen += char
    return dictionary


print(dict_string('adjhfasdjaaa!##!@'))
