import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from stack import stack
from calc import priority

def InToPost(infix):
    s = stack.Stack()
    postfix = []
    for i in infix:
      if i == '(':
        s.push(i)
      elif i == ')':
        while s.peek() != '(':
          postfix.append(s.pop())
        s.pop()
      elif i in priority:
        while not s.is_empty():
          if priority[s.peek()] >= priority[i]:
            postfix.append(s.pop())
          else:
            break
        s.push(i)
      else:
        postfix.append(i)
    while not s.is_empty():
      postfix.append(s.pop())

    return postfix
