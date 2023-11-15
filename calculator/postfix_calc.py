import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from stack import stack
from calculator import calc

def Postfix_calc(postfix):
    st = stack.Stack()
    for cur in postfix:
        if cur in calc.priority:
            operands1 = int(st.pop())
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
