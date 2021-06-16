# 자료 구조의 변경
# 커피숍
menu = {"커피","우유","쥬스"}
print(menu, type(menu))


# 세트를 리스트로 바꿈
menu = list(menu)
print(menu, type(menu))

# 리스트를 튜플로 바꿈
menu = tuple(menu)
print(menu, type(menu))

# 튜플을 세트로 바꿈
menu = set(menu)
print(menu, type(menu))

