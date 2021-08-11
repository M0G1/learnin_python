"""
python 3.9
На любом языке программирования реализовать функцию, принимающую в
качестве входного параметра строку, в которой производится замена всех
первых букв после точек на заглавные
"""
import re

ss = ".a .b asdgasd.e . aasdf"
pattern = re.compile(r"\.([^A-Za-z])*[a-z]")


def upper_match(s: re.Match):
    return s.group().upper()


def up_letter_after_dot(s: str):
    return re.sub(pattern, upper_match, s)

def up_letter_after_dot_simple(s: str):
    answer = ""
    ii = 0
    while ii < len(s):
        if s[ii] == '.':
            while ii < len(s) and not s[ii].isalpha():
                answer = answer + s[ii]
                ii = ii + 1
            answer = answer + s[ii].upper()
            ii = ii + 1
            continue
        answer = answer + s[ii]
        ii = ii + 1
    return answer

print("use re: ", up_letter_after_dot(ss))
print("simple: ", up_letter_after_dot_simple(ss))
