absent = [2, 5] # 결석

no_book = [7] # 책을 안가져옴

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지다. {0}는 교무실로 와라".format(student))
        break
    print("{0}, 책을 읽어라".format(student))