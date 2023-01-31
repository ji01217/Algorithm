def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        kind = cloth[1]
        if kind in dic.keys():
            dic[kind] += 1
        else:
            dic[kind] = 1
    cnts = dic.values()
    for cnt in cnts:
        answer *= cnt + 1
    return answer - 1