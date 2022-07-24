# 입력
first_num = int(input())

# 풀이
ans = 0
result = []

for i in range(first_num + 1):
    result_lst = [first_num, i]
    cnt = 2
    while True:
        last_num = result_lst[cnt - 2] - result_lst[cnt - 1]
        if last_num < 0:
            break
        result_lst.append(last_num)
        cnt += 1
    if ans < len(result_lst):
        ans = len(result_lst)
        result = result_lst[:]

# 출력
print(ans)
print(*result)