import random


# 삐삐호출
def beep(result):
    messages = {
        12486: "012486 : Forever love you!",
        4486: "4486 : I love you even if I die!",
        401: "401 : Love is forever!",
        504: "504 : Only I love you!",
        1052: "1052 : LOVE!",
        1365244: "1365244 : I love you 24 hours a day, 365 days a year!",
        17317071: "17317071 : I love you!",
        1004: "1004 : You are angel!",
        8282: "8282 : Hurry up!",
    }

    result = int(result)

    if result in messages:
        print(messages[result])
    else:
        return


# 제작자 정보
def birth(result):
    # 추가 예정
    list = {
        202018388: "NOH",
        202012237: "IM",
    }

    result = int(result)

    if result in list:
        print(list[result])
    else:
        return


# 잭팟
def jackpot(result):
    result = int(result)
    if result in [111, 222, 333, 444, 555, 666, 777, 888, 999]:
        print(str(result) + " Jackpot!")
    else:
        return
