def solution(array):
    array_copy = array.copy()

    while len(array_copy) != 0:
        for i, a in enumerate(set(array_copy)):
            array_copy.remove(a)
        if i == 0: return a

    return -1