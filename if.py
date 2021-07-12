weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요")

elif weather =="미세먼지":
    print("마스크를 챙기세요")

else:
    print("준비물이 필요없습니다.")

# ----------input 값을 입력한 출력 ------------------------

weather1 =input("오늘 날씨는 어떤가요?!")

if weather1 =="비" or weather1 =="눈":
    print("우산을 챙기세요")

elif weather1 =="미세먼지":
    print("마스크를 챙기세요")

else:
    print("챙길 물품이 없습니다.")

#----------int형 input 값 --------------------------

temp = int(input("기온은 어떄요?"))
if 30<= temp:
    print("너무 더워요. 나가지마세요")
elif 10 <= temp and temp <30:
    print("괜찮은 날씨에요")
elif 0 <=temp and temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지마세요")
