def solution(n):
    result = []
    for i in range(1000):
        if i % 3 != 0 and '3' not in str(i):
            result.append(i)
    return result[n-1]