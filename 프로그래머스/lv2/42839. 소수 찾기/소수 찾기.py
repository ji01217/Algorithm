import math
from itertools import permutations

def solution(numbers):
    answer = 0
    nums = set()
    for i in range(1, len(numbers)+1):
        for j in list(permutations(numbers, i)):
            nums.add(int(''.join(j)))
    max_num = max(nums)
    sieve = [False, False] + [True] * (max_num-1)
    for i in range(2, int(math.sqrt(max_num)+1)):
        if sieve[i] == True:
            for j in range(2*i, max_num+1, i):
                sieve[j] = False
    lst_nums = list(nums)
    for num in lst_nums:
        if sieve[num]:
            answer += 1
    return answer