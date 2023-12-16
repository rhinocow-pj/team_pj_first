import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from easter_egg import easter_egg

priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3, '!':3}
def plus(a, b):
    result = a + b
    return result

def minus(a, b):
    result = a - b
    return result

def multi(a, b):
    result = a * b
    return result

def InPut():
    integers = list('0123456789')
    operators = list('+-*!')

    infix = []
    pre_inpt = [' ', ' ']  # 이전 입력 2개 저장
    while(1):
        cur = input()
        # 이스터에그 확인
        if cur[0] in integers and (easter_egg.beep(cur) or easter_egg.student_id(cur) or easter_egg.jackpot(cur) or easter_egg.school_anniversary(cur)):
            return "easter_egg"
        # input 에러
        if cur in operators and pre_inpt[1][-1] in integers and pre_inpt[0][-1] in integers:
            if cur == '!': return "[ERROR]"
            else: return "[SYSTEM]"
        # factorial 음수 처리
        if (cur == '!' and pre_inpt[1][0] == '-'):
            return "f_error"
        pre_inpt[0] = pre_inpt[1]
        pre_inpt[1] = cur
        
        if cur == '=':
            break
        for i in cur:
            infix.append(i)
    return infix

def Operands(infix):
    numbers = list('0123456789')
    recognized = []

    i = 0
    while i < len(infix):
        j = 1
        if infix[i] in numbers:
            while i + j < len(infix):
                if infix[i + j] in numbers:
                    j += 1
                else:
                    break
            recognized.append(''.join(infix[i:i + j]))
            i += j
        else:
            recognized.append(infix[i])
            i += 1
    return recognized