def solution(numbers):
    lst = list(map(str, numbers))
    lst.sort(key = lambda x: x * 3, reverse = True)
    answer = ''.join(lst)
    return str(int(answer))