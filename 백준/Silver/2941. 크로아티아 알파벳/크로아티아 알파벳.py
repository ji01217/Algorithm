word = input()
ans = 0
l = len(word)
idx = 0
while idx < l:
    if word[idx] == "c":
        if idx < l - 1:
            if word[idx+1] == "=" or word[idx+1] == "-":
                idx += 2
                ans += 1
                continue
    elif word[idx] == "d":
        if idx < l - 2:
            if word[idx+1] == "z" and word[idx+2] == "=":
                idx += 3
                ans += 1
                continue
            if word[idx+1] == "-":
                idx += 2
                ans += 1
                continue
        elif idx < l - 1:
            if word[idx+1] == "-":
                idx += 2
                ans += 1
                continue
    elif word[idx] == "l":
        if idx < l - 1:
            if word[idx+1] == "j":
                idx += 2
                ans += 1
                continue
    elif word[idx] == "n":
        if idx < l - 1:
            if word[idx+1] == "j":
                idx += 2
                ans += 1
                continue
    elif word[idx] == "s":
        if idx < l - 1:
            if word[idx+1] == "=":
                idx += 2
                ans += 1
                continue
    elif word[idx] == "z":
        if idx < l - 1:
            if word[idx+1] == "=":
                idx += 2
                ans += 1
                continue
    idx += 1
    ans += 1
print(ans)