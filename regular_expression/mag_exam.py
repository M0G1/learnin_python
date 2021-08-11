"""
python 3.9
На любом языке программирования реализовать функцию, принимающую в
качестве входного параметра строку, в которой производится замена всех
первых букв после точек на заглавные
"""

import re

ss = ".a .b asdgasd.e"
pattern = re.compile(r"\.[a-z]")


def upper_match(s: re.Match):
    return s.group().upper()


def up_letter_after_dot(s: str):
    return re.sub(pattern, upper_match, s)


def up_letter_after_dot_simple(s: str):
    ans = s[0]
    for i in range(1, len(s)):
        if s[i - 1] == "." and ("a" <= s[i] <= "z"):
            ans = ans + s[i].capitalize()
        else:
            ans = ans + s[i]
    return ans


print("use re: ", up_letter_after_dot(ss))
print("simple: ", up_letter_after_dot_simple(ss))
