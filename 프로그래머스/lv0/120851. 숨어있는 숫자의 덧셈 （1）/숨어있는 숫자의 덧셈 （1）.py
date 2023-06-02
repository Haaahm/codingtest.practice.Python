import re

def solution(my_string):
    return sum(int(i) for i in re.sub('[^1-9]', '', my_string))