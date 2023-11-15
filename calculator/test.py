import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from calc import Operands, InPut
from intopost import InToPost
from postfix_calc import Postfix_calc
from errorfinder import error_finder
from easteregg import easter_egg


while True:
   print("수식을 입력해주세요")
   test_data = InPut()

   infix = Operands(test_data)
   postfix = InToPost(infix)
   result = Postfix_calc(postfix)

   if error_finder(test_data) != None:
       print(error_finder(test_data))
       continue
   elif(test_data == []):
       print("피연산자 중복오류")
       continue

   if(len(infix) == 1):
       easter_egg.beep(result)
       easter_egg.birth(result)
       easter_egg.jackpot(result)
   else:
       print(result)
