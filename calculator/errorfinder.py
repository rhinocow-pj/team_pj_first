from stack import stack

def error_finder(test_data):
    input_data = list('0123456789()+-')
    integers = list('0123456789')
    operators = list('+-')
    s = stack.Stack()

    for i in range(len(test_data)):
        if test_data[i] not in input_data:
            return i
        elif i == 0 and test_data[i] in operators:
            return i
        elif test_data[i] in operators:
            if i + 1 == len(test_data):
                return i
            else:
                if test_data[i + 1] in operators:
                    return i + 1
        elif test_data[i] == '(':
            if test_data[i - 1] in integers and i != 0:
                return i
            else:
                if s.is_empty():
                    s.push('(')
                else:
                    return i
        elif test_data[i] == ')':
            if s.is_empty():
                return i
            elif test_data[i + 1] in integers and i != len(test_data) - 1:
                return i + 1
            else:
                s.push(')')

    if not s.is_empty():
        if s.pop() == '(':
            return len(test_data)
