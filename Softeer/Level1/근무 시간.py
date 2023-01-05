arr = [input() for _ in range(5)]
ans = 0
for i in arr:
    ans += (int(i[6:8])-int(i[0:2]))*60 + int(i[9:]) - int(i[3:5])
print(ans)