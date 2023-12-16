from stack import stack

def error_finder(test_data):
    input_data = list('0123456789()+-*!')
    integers = list('0123456789')
    operators = list('+-*')
    s = stack.Stack()

    for i in range(len(test_data)):
        if test_data[i] not in input_data:
            return "입력은 정수 또는 지정된 연산자(+,-,*)만 입력가능합니다."
        elif i == 0 and test_data[i] in operators:
            return "연산자가 처음으로 입력되었습니다."
        elif test_data[i] in operators:
            if i + 1 == len(test_data):
                return "입력을 제대로 해주세요."
            else:
                if test_data[i + 1] in operators:
                    return "연산자 중복오류"
        elif test_data[i] == '(':
            if test_data[i - 1] in integers and i != 0:
                return "괄호처리 오류"
            else:
                if s.is_empty():
                    s.push('(')
                else:
                    return "괄호처리 오류"
        elif test_data[i] == ')':
            if s.is_empty():
                return "괄호처리 오류"
            elif test_data[i + 1] in integers and i != len(test_data) - 1:
                return "괄호처리 오류"
            else:
                s.push(')')

    if not s.is_empty():
        if s.pop() == '(':
            return len(test_data)
