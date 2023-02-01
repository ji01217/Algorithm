def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in range(len(tangerine)):
        if tangerine[i] in dic.keys():
            dic[tangerine[i]] += 1
        else:
            dic[tangerine[i]] = 1
    values = sorted(dic.values(), reverse=True)
    cnt = 0
    while cnt < k:
        cnt += values[answer]
        answer += 1
    return answer