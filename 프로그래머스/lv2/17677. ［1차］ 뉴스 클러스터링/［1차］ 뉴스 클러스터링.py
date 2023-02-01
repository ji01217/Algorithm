def solution(str1, str2):
    answer = 1
    s1 = len(str1)
    s2 = len(str2)
    lst1 = []
    lst2 = []
    for i in range(s1-1):
        if (65 <= ord(str1[i]) <= 90 or 97 <= ord(str1[i]) <= 122) and (65 <= ord(str1[i+1]) <= 90 or 97 <= ord(str1[i+1]) <= 122):
            lst1.append((str1[i].lower(), str1[i+1].lower()))
    for i in range(s2-1):
        if (65 <= ord(str2[i]) <= 90 or 97 <= ord(str2[i]) <= 122) and (65 <= ord(str2[i+1]) <= 90 or 97 <= ord(str2[i+1]) <= 122):
            lst2.append((str2[i].lower(), str2[i+1].lower()))
    l1 = len(lst1)
    l2 = len(lst2)
    hap = l1 + l2
    gyo = 0
    for i in range(l1):
        for j in range(l2):
            if lst1[i] and lst2[j] and lst1[i] == lst2[j]:
                lst1[i], lst2[j] = (), ()
                hap -= 1
                gyo += 1
    if hap != 0:
        answer = (gyo / hap)
    return int(answer * 65536)