N = int(input())
lst = []
for _ in range(N):
    age, name = input().split()
    lst.append([int(age), name])
lst.sort(key= lambda x: x[0])
for i in range(N):
    print(lst[i][0], lst[i][1])