# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 2분

from random import *

customer = []
cnt = 0


for i in range(0,50):
    customer.insert(i,randint(5,50))

for i in range(0,50):
    if customer[i]>=5 and customer[i]<=15 :
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i+1,customer[i]))
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i+1,customer[i]))

