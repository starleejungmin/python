#print("대기번호 : 1")
#print("대기번호 : 2")
#print("대기번호 : 3")
#print("대기번호 : 4")
#print("대기번호 : 5")

for waitno in [0,1,2,3,4]: # 특정한 값을 입력 받아야 하는경우 사용
    print("대기번호: {0}".format(waitno))

for waitno in range(5): # 0~4까지 range 값을 가져와서 출력한다.
    print("대기번호: {0}".format(waitno))

for waitno in range(1, 6): # 1~5까지의 range 값을 가져와서 출력한다.
    print("대기번호:{0}".format(waitno))


sb = ["아이언맨", "토르", "아이엠 그루트"] # 인자 값을들 반복적으로 붙여서 출력한다.
for sb2 in sb:
    print("{0}, 커비가 준비되었습니다".format(sb2))