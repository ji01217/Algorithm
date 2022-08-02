# 입력
n = int(input())
students = [input().split() for _ in range(n)]

# 풀이
sorted_students = sorted(students, key = lambda x : (int(x[3]), int(x[2]), int(x[1])))

# 출력
print(sorted_students[n - 1][0])
print(sorted_students[0][0])