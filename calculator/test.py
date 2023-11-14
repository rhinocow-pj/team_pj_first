import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from calc import Operands, InPut
from intopost import InToPost
from postfix_calc import Postfix_calc
from errorfinder import error_finder
from easter_egg import easter_egg


while True:
   print("입력받기")
   test_data = InPut()
   if error_finder(test_data) != None:
       print(error_finder(test_data))
       continue
   elif(test_data == []):
       print("피연산자 중복오류")
       continue

   infix = Operands(test_data)
   postfix = InToPost(infix)

   print(postfix)

   result = Postfix_calc(postfix)
   print(result)

   easter_egg.beep(result)
   easter_egg.birth(result)
   easter_egg.jackpot(result)
