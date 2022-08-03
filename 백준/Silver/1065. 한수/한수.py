# 풀이
def hansu(num):
    ans = 99
    if num < 100:
        ans = num
        return ans
    for i in range(100, num + 1):
        num_lst = list(map(int, str(i)))
        if num_lst[0] - num_lst[1] == num_lst[1] - num_lst[2]:
            ans += 1
    return ans

# 입력
N = int(input())

# 출력
print(hansu(N))