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


def task5():
    inpu = """1.2 
  1. 
    1.0e-55  
      e-12   
  6.5E 
        1e-12  
  +4.1234567890E-99999           
  7.6e+12.5 
   99 """

    pattern = re.compile(r"[+-]?\d+(?:(?:\.\d+)|(?:\.\d+)?(?:[eE][+-]?\d+))")

    for s in inpu.split():
        m = re.fullmatch(pattern, s)
        if m is not None:
            print(s, "is legal")
        else:
            print(s, "is illegal")


def task6():
    inpu = """Это курс информатики соответствует ФГОС и ПООП, 
это подтверждено ФГУ ФНЦ НИИСИ РАН"""

    pattern = re.compile(r"[А-Я]{2,}(?:\s[А-Я]{2,})*")

    res = re.findall(pattern, inpu)
    print(len(res), type(res))
    for ii in res:
        print("\t", ii, "\t", type(ii), len((ii)))


def task7():
    inpu = """Было закуплено 12 единиц техники 
по 410.37 рублей"""

    pattern = re.compile(r"\d+")

    def match_handle(m: re.Match):
        digit = int(m.group())
        digit = digit ** 3
        return str(digit)

    ans = re.sub(pattern, match_handle, inpu)
    print(ans)


def task8():
    inpu = ("""Московский государственный институт международных отношений""",
            """микоян авиацию снабдил алкоголем, 
народ доволен работой авиаконструктора""")

    pattern = re.compile(r"\b[А-Яа-яёЁ]")
    for ss in inpu:
        ans = ("".join(re.findall(pattern, ss))).upper()
        print(ans)


def task9():
    inpu = ("Вечер за окном. / Еще один день прожит. / Жизнь скоротечна...",
            "Просто текст",
            "Как вишня расцвела! / Она с коня согнала / И князя-гордеца.",
            "На голой ветке / Ворон сидит одиноко… / Осенний вечер!",
            "Тихо, тихо ползи, / Улитка, по склону Фудзи, / Вверх, до самых высот!",
            "Жизнь скоротечна… / Думает ли об этом / Маленький мальчик.")

    pattern = re.compile(r"[ёЁуУеЕыЫаАоОэЭяЯиИюЮ]")

    syllable = (5, 7, 5)
    for ss in inpu:
        splitted = ss.split("/ ")
        if len(splitted) != 3:
            print("Не хайку. Должно быть 3 строки.")
            continue

        for ii in range(3):
            count = len(re.findall(pattern, splitted[ii]))
            if count != syllable[ii]:
                print(f"Не хайку. В {ii + 1} строке слогов не {syllable[ii]}, а {count}.")
                break
        else:
            print("Хайку!")


if __name__ == '__main__':
    task9()
