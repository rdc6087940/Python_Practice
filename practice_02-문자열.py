python = "Python is Amazing"

print(python.lower()) #소문자 변환
print(python.upper()) #대문자 변환
print(python[0].isupper()) #0번째 글자 대문자인지 검사
print(len(python)) # 문자열 길이 출력
print(python.replace("Python", "Java")) # 특정문자열을 찾아 지정문자열로 치환

index = python.index("n") # 찾으려는 문자열의 위치를 반환
print(index)

index2 = python.index("n", index+1) # 두번째 n 을 찾게됨
print(index2)

print(python.find("n")) # 문자열.index 와 마찬가지로 

print(python.find("Java"))  # index와 다른점은 원하는 값이 없으면
                            #-1을 반환
# print(python.index("Java")) # index는 에러가 반환된다.

print(python.count("n")) # 문자열에서 지정한 문자의 개수

#### 문자열 포맷
print("a" + "b")    # ab
print("a","b")      # a b

# 방법 1
print("나는 %d살입니다."% 20)
print("나는 %s를 좋아해요."% "파이썬")
print("Apple 이라는 단어는 %c로 시작해요"% "A")

# %s 
print("나는 %s살입니다."% 20)

print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간"))

# 방법 3
print("나는 {age} 살이며, {color}색을 좋아해요".format(age=20,color="빨간"))
print("나는 {color} 살이며, {age}색을 좋아해요".format(age=20,color="빨간"))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age} 살이며, {color}색을 좋아해요")

## 탈출문자 \n : 줄바꿈
print("백문이 불여일견 \n벽견이 불여일타")

# \" \'
# 저는 "나도코딩" 입니다. 
print("저는 '나도코딩' 입니다.")
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")

# \\ : 문장 내에서 \
# print("C:\Users\kosmo_\Desktop\Pythonworkspace")
print("C:\\Users\\kosmo_\\Desktop\\Pythonworkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t :탭
print("Red\tApple")