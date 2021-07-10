# 리스트 []

#지하철 칸별로 10명, 20명, 30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]

print(subway)

subway =["유재석","조세효","박명수"]
print(subway)

#조세호 씨는 몇번째 칸에 타고 있는가?!
print(subway.index("유재석"))

#하하씨가 다음 정류장에서 탑승함.
subway.append("하하")  #  리스트에 추가하는 함수 .append
print(subway)

#정횬돈씨를 유재석 / 조세효 사이에 태워봄
subway.insert(1,"정형돈") #정형돈을 1번째 방에 포함시켜라
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

#같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능 순서대로
num_list=[5,3,6,4,1]
print(num_list)
num_list.sort()
print(num_list)

#순서 뒤집기 역순
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함게 사용
mix_list=("조세호", 20, 20>30)
print(mix_list)
print()

# 리스트 확장
num_list.extend(mix_list)
print(num_list)