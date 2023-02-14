N = int(input())
ans = 0
for i in range(N):
    word = input()
    error = 0
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if word[j] in new_word:
                error += 1
                break
    if error == 0:
        ans += 1

print(ans)