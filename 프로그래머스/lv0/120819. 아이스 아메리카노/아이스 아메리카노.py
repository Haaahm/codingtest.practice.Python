def solution(money):
    return [money//5500, money%5500]

# 다른 방법 메모하기!
def solution(money):
    return divmod(money, 5500) # divmod 함수는 (몫, 나머지) 형태의 튜플을 반환한다. 
