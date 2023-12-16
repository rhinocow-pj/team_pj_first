# TDD 접근 방법
# 가짜 구현 -> 삼각 측량법 -> 명백한 구현

from calculator import calc

# 명백한 구현
def factorial(a):
    # 음수 팩토리얼 -> 에러처리
    # if (a < 0): return -1
    # 입력 시 처리를 위해 Input에서 처리 후 main에서 처리하는 것으로 수정

    # 두 개 이상의 숫자 입력 -> 에러처리
    # calc에 Input()에서 처리 후 main에서 에러

    if (a == 0 or a == 1):
        return 1

    return calc.multi(a, factorial(a-1))

# def factorial_test():
#     while (1):
#         inpt = input()

#         result = factorial(int(inpt)) # inpt

#         if (result == -1): print("[ERROR] Out Of Range")
#         else: print(result)
    
#     return 0

# factorial_test()