def solution(nums):
    answer = 0
    kinds = len(set(nums))
    cnt = len(nums) // 2
    if kinds <= cnt:
        answer = kinds
    else:
        answer = cnt
    return answer