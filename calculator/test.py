import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from stack import stack
from calc import plus, minus, multi, Operands
from intopost import InToPost
from postfix_calc import Postfix_calc
from errorfinder import error_finder

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
 test_data = list(input("스택을 이용해 연산 숫서 결정하기위한 함수 테스팅 입력 예) (2+3)*4:" ))
 infix = Operands(test_data)
 postfix = InToPost(infix)
 print(postfix)
 print(Postfix_calc(postfix))
 if error_finder(test_data) != None:
    print("수식에 오류가 있습니다! 수식을 다시 확인해주세요!")
    continue
