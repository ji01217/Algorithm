N = int(input())
dot = 3
for i in range(1, N):
    dot = (dot - 1) * 2 + 1
print(dot*dot)