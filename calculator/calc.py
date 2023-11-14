import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}
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
    infix = []
    while(1):
        cur = input()
        if(cur == '='):
            break
        infix.append(cur)
    return infix
