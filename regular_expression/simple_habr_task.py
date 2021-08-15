"""
https://habr.com/ru/post/349860/
"""

import re


def task1():
    inpu = """С227НА777 
КУ22777 
Т22В7477 
М227К19У9 
 С227НА777"""

    pattern_priv = re.compile(r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{3}")
    pattern_taxi = re.compile(r"[АВЕКМНОРСТУХ]{2}\d{5}")

    def f(s: str):
        print(s)
        if re.match(pattern_priv, s) is not None:
            return "\tprivate"
        elif re.match(pattern_taxi, s) is not None:
            return "\ttaxi"
        return "\tfail"

    for s in inpu.split("\n"):
        print(f(s))


def task2():
    inpu = """Он --- серо-буро-малиновая редиска!! 
>>>:-> 
А не кот. 
www.kot.ru"""
    pattern = re.compile(r"([A-Za-zА-Яа-яёЁ]+-?[A-Za-zА-Яа-яёЁ]+)+")
    ans = len(re.findall(pattern, inpu))
    print(ans)


def task3():
    inpu = ("""Иван Иванович! 
Нужен ответ на письмо от ivanoff@ivan-chai.ru. 
Не забудьте поставить в копию 
serge'o-lupin@mail.ru- это важно.""", """
NO: foo.@ya.ru, foo@.ya.ru 
PARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru""")

    pattern = re.compile(r"[A-Za-z0-9'_]+[A-Za-z0-9'_.+-]*[A-Za-z0-9'_]+@[A-Za-z0-9]+[A-Za-z0-9.-]*[A-Za-z0-9]+")

    for ss in inpu:
        ans = re.findall(pattern, ss)
        for ii in range(len(ans)):
            print(f"\t{ans[ii]}")
        else:
            print()


def task4():
    inpu = """Уважаемые! Если вы к 09:00 не вернёте 
чемодан, то уже в 09:00:01 я за себя не отвечаю. 
PS. С отношением 25:50 всё нормально!"""

    pattern = re.compile(r"(?:[0-1][0-9]|2[0-3])(?::[0-5][0-9]){1,2}")

    ans = re.sub(pattern, "(TBD)", inpu)
    print(ans)


if __name__ == '__main__':
    task4()
