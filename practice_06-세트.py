# 집합 (세트)
# 중복이 안되고, 순서가 없음

# 세트의 형식
my_set = {1,2,3,3,3}
print(my_set)
# 출력해보면 중복된 '3' 값이 하나만 출력되는것을 알 수 있다.

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

# 교집합 (java 와 python 을 모두할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java 나 python 둘 중 하나라도 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합 (java 는 할 수 있지만 python 은 못하는 사람)
print(java - python)
print(java.difference(python))

# python 을 할 줄 아는 사람이 늘어났을때
python.add("김태호")
print(python)

# python 을 까먹음
python.remove("김태호")
print(python)