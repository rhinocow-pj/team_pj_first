import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from calculator import calc, errorfinder, intopost, postfix_calc

while True:
   print("수식을 입력해주세요")
   test_data = calc.InPut()

   if(test_data == "easter_egg"):
       continue
   elif(test_data == "error"):
       print("피연산자 중복오류")
       continue
   elif errorfinder.error_finder(test_data) != None:
       print(errorfinder.error_finder(test_data))
       continue
   
   infix = calc.Operands(test_data)
   postfix = intopost.InToPost(infix)
   result = postfix_calc.Postfix_calc(postfix)

   if(len(infix) != 1):
       print(result)
