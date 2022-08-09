# 입력
T = int(input())

# 풀이
for i in range(T):
    stack = []
    PS = input()
    for j in PS:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')