python = "Ptyhon is Amazing"
print(python.lower()) # lower 은 소문자로 출력할수있음
print(python.upper()) # Uoper 은 모두 대문자로 출력함.
print(python[0].isupper()) # 첫번쨰 자리수가 대문자인지? 불리안형으로 출력
print(len(python)) # 총길이를 출력하는 문자열
print(python.replace("Ptyhon", "java")) #replace 문자열의 값을 변경해서 출력해주는 함수


index =python.index("n") # pyrhon 변수에 n이 몇번쨰 인지 알려준다.
print(index)
index =python.index("n", index +1) # index 값에 +1 하면 다음번에 N값을 출력한다.
print(index)

print(python.find("java")) # Find yhthon 변수안에 특정 값이 없다면 -1을 반환한다.

print(python.count("n"))# count 는 특정값이 몇번 출력되는지 확인