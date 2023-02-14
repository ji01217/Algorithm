def delete(word):
    l = len(word)
    for i in range(l-1):
        if word[i] == word[i+1]:
            word = word[:i] + word[i+1:]
            word = delete(word)
            return word
    return word



N = int(input())
ans = 0
for i in range(N):
    word = input()
    new = delete(word)
    al = set()
    l = len(new)
    for j in range(l):
        if new[j] in al:
            break
        al.add(new[j])
        if j == l - 1:
            ans += 1

print(ans)