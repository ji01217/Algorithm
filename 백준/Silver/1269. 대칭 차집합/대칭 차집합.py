# 입력
lenA, lenB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 풀이
hap = set()
hap.update(A)
hap.update(B)
ans = lenA + lenB - (lenA + lenB - (len(hap))) * 2

# 출력
print(ans)