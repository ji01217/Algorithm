T = int(input())
arr = [list(input().split()) for _ in range(T)]
led = ['1110111', '0010010', '1011101', '1011011', '0111010', '1101011', '1101111', '1110010', '1111111', '1111011']
for t in range(T):
    a = arr[t][0]
    b = arr[t][1]
    ans = 0
    if len(a) == len(b):
        for i in range(len(a)):
            for j in range(7):
                if led[int(a[i])][j] != led[int(b[i])][j]:
                    ans += 1
    elif len(a) > len(b):
        dif = len(a) - len(b)
        for i in range(dif):
            ans += led[int(a[i])].count('1')
        for i in range(len(b)):
            for j in range(7):
                if led[int(a[i+dif])][j] != led[int(b[i])][j]:
                    ans += 1
    else:
        dif = len(b) - len(a)
        for i in range(dif):
            ans += led[int(b[i])].count('1')
        for i in range(len(a)):
            for j in range(7):
                if led[int(a[i])][j] != led[int(b[i+dif])][j]:
                    ans +=1
    print(ans)