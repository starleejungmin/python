#출석번호가 1 2 3 4 , 앞에 100을 붙이기로함 -> 101 , 102 ,103 , 104

student = [1,2,3,4,5]
print(student)

student =[i+100 for i in student] # 
print(student)

# 학생 이름을 길이로 변환

student =["Iron man" , "Thor", "i am groot"]
print(student)

student =[len(i) for i in student]
print(student)

#학생 이름을 대문자로 변환

student =["Iron man" , "Thor", "i am groot"]
student =[i.upper() for i in student]
print(student)