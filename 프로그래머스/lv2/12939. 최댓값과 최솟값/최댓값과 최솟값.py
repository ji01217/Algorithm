def solution(s):
    lst = list(map(int, s.split()))
    ma = max(lst)
    mi = min(lst)
    answer = str(mi) + ' ' + str(ma)
    return answer