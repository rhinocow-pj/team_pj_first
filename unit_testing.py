from calculator import calc, factorial
from stack import stack
import unittest

def error_finder(test_data):
    input_data = list('0123456789()+-*!')
    integers = list('0123456789')
    operators = list('+-*')
    s = stack.Stack()

    for i in range(len(test_data)):
        if test_data[i] not in input_data:
            return "[SYSTEM]입력은 정수 또는 지정된 연산자(+,-,*)만 입력가능합니다."
        elif i == 0 and test_data[i] in operators:
            return "[SYSTEM]연산자가 처음으로 입력되었습니다."
        elif test_data[i] in operators:
            if i + 1 == len(test_data):
                return "[SYSTEM]입력을 제대로 해주세요."
            else:
                if test_data[i + 1] in operators:
                    return "[SYSTEM]연산자 중복오류"
        elif test_data[i] == '(':
            if test_data[i - 1] in integers and i != 0:
                return "[SYSTEM]괄호처리 오류"
            else:
                if s.is_empty():
                    s.push('(')
                else:
                    return "[SYSTEM]괄호처리 오류"
        elif test_data[i] == ')':
            if s.is_empty():
                return "[SYSTEM]괄호처리 오류"
            elif test_data[i + 1] in integers and i != len(test_data) - 1:
                return "[SYSTEM]괄호처리 오류"
            else:
                s.push(')')

    if not s.is_empty():
        if s.pop() == '(':
            return len(test_data)

def student_id(result):
    # 추가 예정
    list = {
        "202018388" : "NOH",
        "202012237" : "IM",
        "202118020" : "KIM",
        "202012259" : "HONG",
        "202018416" : "HEO",
        "202012249" : "JO",
        "201010613" : "Park"
    }

    if result in list:
        #유닛테스팅을 위한 코드 수정. 기존 : print("[EVENT]"+list[result])
        return True
    else:
        return False

def Postfix_calc(postfix):
    st = stack.Stack()
    for cur in postfix:
        if cur in calc.priority:
            operands1 = int(st.pop())

            if cur == '!':
                st.push(factorial.factorial(operands1))
                continue

            operands2 = int(st.pop())
            if cur == '+':
                st.push(calc.plus(operands2, operands1))
            elif cur == '-':
                st.push(calc.minus(operands2, operands1))
            elif cur == '*':
                st.push(calc.multi(operands2, operands1))
        else:
            st.push(cur)
    return st.pop()

class TestCapErrorFinder(unittest.TestCase):
    def test_error_finder_1(self):
        input = "5/9+4"
        self.assertEqual("[SYSTEM]입력은 정수 또는 지정된 연산자(+,-,*)만 입력가능합니다.", error_finder(input))
    def test_error_finder_2(self):
        input = "+9*11"
        self.assertEqual("[SYSTEM]연산자가 처음으로 입력되었습니다.", error_finder(input))
    def test_error_finder_3(self):
        input = "9*+11"
        self.assertEqual("[SYSTEM]연산자 중복오류", error_finder(input))

class TestCapStudentnumber(unittest.TestCase):
    def test_student_number_1(self):
        input = "202012237"
        self.assertTrue(student_id(input))
    def test_student_number_2(self):
        input = "212012237"
        self.assertFalse(student_id(input))

class TestCapPostToFix(unittest.TestCase):
    def test_error_finder_plus(self):
        input = "95+"
        result = Postfix_calc(input)
        self.assertEqual(result, 14)
    def test_error_finder_minus(self):
        input = "95+8-"
        result = Postfix_calc(input)
        self.assertEqual(result, 6)
    def test_error_finder_multi(self):
        input = "853*-9+"
        result = Postfix_calc(input)
        self.assertEqual(result, 2)
    def test_error_finder_fact(self):
        input = "4!"
        result = Postfix_calc(input)
        self.assertEqual(result, 24)

if __name__ == '__main__':
    unittest.main(exit=False)
