import calc
import sys

from intopost import InToPost
from easter_egg import beep
from easter_egg import birth
from easter_egg import jackpot

# TODO
"""
1. Enter로 입력을 받는다.

2. 지원하는 연산은 더하기(+), 빼기(-), 곱하기(*)다.

3. 한 번의 입력에는 한 종류의 연산만 들어올 수 있다.

4. 사용자가 =를 입력하면 연산 결과를 출력한다.

5. 정수만 입력될 수 있다.

6. 2-5번의 입력 외에는 에러메세지를 출력한다.
"""


""" value definition here """
type_exeption = ["(", ")", "+", "-", "*"]
is_division = False


""" Function definition here """
def split_user_input(user_input_string: str) -> list:
    buffer = ""
    changing_result = []
    for index in range(len(user_input_string)):

        if index == 0 and user_input_string[index] == '-':
            buffer += user_input_string[index]
            continue

        if user_input_string[index] not in type_exeption:
            buffer += user_input_string[index]

        else:
            changing_result.append(buffer)
            changing_result.append(user_input_string[index])
            buffer = ""

    changing_result.append(buffer)

    return changing_result


def processing_easter_egg(number: int) -> None:
    beep(number)
    birth(number)
    jackpot(number)

    return None

while True:
    user_input_exprssion = sys.stdin.readline().rstrip()
    # EOF detection, end state processing here
    try:
        if user_input_exprssion[0] == "=":
            break
    except IndexError:
        print("EOF Error occured, Please try again")
        continue


    # Split user input based on four-pronged operation symbols
    user_input_exprssion = user_input_exprssion.replace(" ", "")
    user_input_exprssion = split_user_input(user_input_exprssion)

    # Change type of string to decimal
    for idx in range(len(user_input_exprssion)):
        # detection easter_egg here
        processing_easter_egg(user_input_exprssion[idx])

        # division detection code here
        if user_input_exprssion[idx] == '/':
            is_division = True

        # checking condition 5. which in TODO here
        if user_input_exprssion[idx] not in type_exeption:
            try:
                user_input_exprssion[idx] = int(user_input_exprssion[idx])
            except ValueError:
                print("Please check your input, You can only type the int")
                break


    # Division error processing
    if is_division:
        print("We do not support division, Sorry bro")
        is_division = False
        continue


    # Result about infix
    infix = user_input_exprssion


    # Call out InToPost function here (for debug)
    InToPost(infix)
