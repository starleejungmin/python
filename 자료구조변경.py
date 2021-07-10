#자료구조 변경
#커피숍
from typing import Text


menu={"커피", "우유","주스"} #class 는 set으로 설정됨
print(menu,type(menu))

menu=list(menu)
print(menu,type(menu)) # 자료형을 list로 변환시킴

menu=tuple(menu)
print(menu,type(menu)) #자료형을 tuple로 변환시킴

menu=set(menu) # 자료형을 다시 set으로 변환시킴
print(menu,type(menu))