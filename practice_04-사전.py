cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))
# [n] 과 get(n) 의 차이
# [n] 같은 경우는 해당하는 키값에 데이터가 들어있지 않은 경우에
# 에러를 발생하지만 get(n)은 데이터가 들어있지 않은 경우 None 을
# 출력한다.

# 뒤에 , "문자열" 로 default 값을 줄 수 있다.
print(cabinet.get(5, "사용 가능"))

# 3 이라는 키가 cabinet 에 있는가
print(3 in cabinet)     # true
print(5 in cabinet)     # false

# 키에 해당하는 값을 숫자말고도 가능하다
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
# "C-20" 이라는 키에 "조세호" 을 넣는다.
# 이미 "C-20" 이라는 키를 사용하고 있으면 업데이트한다.
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "김종국"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)


# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, values 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
