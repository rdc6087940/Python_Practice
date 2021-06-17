def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


def deposit(balance, money):    #입금
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):   #출금
    if balance>= money :
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100    # 수수료
    if balance>= money+100 :
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance-money-commission))
        return commission,balance-money-commission
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance



balance =0
balance = deposit(balance,10000)
print(balance)

balance = withdraw(balance,2000)
balance = withdraw(balance,500)
print(balance)

commission, balance = withdraw_night(balance,300)
print("수수료는 {0} 원이고 잔액은 {1}원 입니다.".format(commission, balance))
