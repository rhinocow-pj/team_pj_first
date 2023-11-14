import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from stack import stack
from calc import plus, minus, multi, InPut
from intopost import InToPost
from postfix_calc import Postfix_calc
from errorfinder import error_finder
from easter_egg import easter_egg

# print("연동 테스트파일입니다.")
# print("1.+,-,* 테스트를 위한 두개의 숫자 입력")
#
#
# # a = int(input())
# # b = int(input())
# # c = plus(a,b)
# # d = minus(a,b)
# # f = multi(a,b)
# # print(c,d,f)


# test_data = list(input("스택을 이용해 연산 숫서 결정하기위한 함수 테스팅 입력 예) (2+3)*4:" ))
# infix = Operands(test_data)
# postfix = InToPost(infix)
# print(postfix)
# print(Postfix_calc(postfix))

while True:
     print("입력받기")
     infix = InPut()
     easter_egg.beep(infix[:-1])
     easter_egg.birth(infix[:-1])
     easter_egg.jackpot(infix[:-1])
     if error_finder(infix) != None:
        print("수식에 오류가 있습니다! 수식을 다시 확인해주세요!")
        continue

     postfix = InToPost(infix)
     print(postfix)
     print(Postfix_calc(postfix))
