import sys

N = int(input())

nums = []
hap = 0
lst = [0] * 8001
idx = []
count = 0

for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
    hap += num
    lst[num] += 1
    if lst[num] > count:
        idx = [num]
        count = lst[num]
    elif lst[num] == count:
        idx.append(num)

# 산술평균
print(round(hap/N))

# 중앙값
nums.sort()
print(nums[N//2])

# 최빈값
if len(idx) == 1:
    print(idx[0])
else:
    idx.sort()
    print(idx[1])

# 범위
print(nums[-1]-nums[0])
