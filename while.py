#while

CM="토르"
index = 5
while(index >=1):
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았습니다".format(CM,index))
    index -=1
    if index ==0:
        print("커피가 폐기처분되었습니다.")


# CM2="아이언맨"
# index2 = 6
# while True:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았습니다".format(CM2,index2)) #무한 루프 된다.

CM3 ="토르"
person ="unknown"

while person != CM3:
    print("{0},커피가 준비되었습니다".format(CM3))
    person =input("이름이 어떻게되세요?")
