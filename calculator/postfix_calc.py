import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from stack import stack
from calc import plus, minus, multi, priority

def Postfix_calc(postfix):
    st = stack.Stack()
    for cur in postfix:
        if cur in priority:
            operands1 = int(st.pop())
            operands2 = int(st.pop())
            if cur == '+':
                st.push(plus(operands2, operands1))
            elif cur == '-':
                st.push(minus(operands2, operands1))
            elif cur == '*':
                st.push(multi(operands2, operands1))
        else:
            st.push(cur)
    return st.pop()
