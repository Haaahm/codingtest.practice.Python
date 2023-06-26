def solution(slice, n):
    for i in range(51):
        if n <= i * slice:
            break
    return i