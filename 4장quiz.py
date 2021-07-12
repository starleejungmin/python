# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기를 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게됩니다.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 :[2,3,4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# list =[1,2,3,4,5]
# print(list)
# shuffle(list) # shuffle list안에 값을 섞어서출력
# print(list)
# print(sample(list,1)) #sample list안에 임의의 값 1개 출력

from random import *
user = range(1, 21)
user =list(user)
print(user)
shuffle(user)
print(user)

winner =sample(user,4)
print(winner)

print("당첨자 발표 --")
print("치킨 당첨자: {0}".format(winner[0]))
print("커피당첨자: {0}".format(winner[1:]))
print("-- 축하합니다 --")
print("-- 당첨자 발표--")