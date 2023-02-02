def solution(participant, completion):
    dic = {}
    sum_hash = 0
    for part in participant:
        dic[hash(part)] = part
        sum_hash += hash(part)
    for com in completion:
        sum_hash -= hash(com)
    return dic[sum_hash]