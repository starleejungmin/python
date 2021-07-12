adsent = [2,5] #결석

no_book =[7] # 책을 깜빡했음

for student in range(1,10):
    if student in adsent:
        continue
    if student in no_book:
        print("오늘수업 여기까지 . {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
