def solution(s):
    p = y = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i]=='P':
            p += 1
        if s[i] == 'y' or s[i]=='Y':
            y += 1
    if p == y:
        return True
    else:
        return False