import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}
def plus(a, b):
    a = int(a)
    b = int(b)
    result = a + b
    return result


def minus(a, b):
    a = int(a)
    b = int(b)
    result = a - b
    return result


def multi(a, b):
    a = int(a)
    b = int(b)
    result = a * b
    return result


def Operands(infix):
    numbers = list('0123456789.')
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
