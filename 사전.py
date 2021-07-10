cabinet = {3:"유재석", 100:"이정민"} # key : value 로 구성한다.
print(cabinet[3])
print(cabinet[100])
print(cabinet[3],cabinet[100])
print(cabinet.get(3))

#[] , get 의차이

# print(cabinet[5]) # 해당 위치에서 프로그램 종료
# print("프로그램종료됨을확인") #

print(cabinet.get(5)) #None 으로 출력된다.
print(cabinet.get(5),"사용가능")
print("종료 안됨확인")

#key 가 있는지 확인하는 방법

print(3 in cabinet) #True
print(5 in cabinet) #Fale

#문자열도 가능
cabinet = {"A-3":"유재석","B-100":"이정민"}
print(cabinet.get("A-3"))

#새 손님
cabinet["C-30"] ="김아람"
print(cabinet) #새로운 변수값이 들어가는지확인한다.
cabinet["C-30"] ="변화확인"
print(cabinet)

#삭제 하는방법
del cabinet["A-3"] # 변수안에 있는 값을 삭제한다.
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key value 쌍으로 출력
print(cabinet.items())

#변수값을 모두 삭제
cabinet.clear()
print(cabinet)