def solution(s):
    dic = {}
    for i in range(1, len(s)-1):
        if s[i] == "{":
            tem = set()
            num = ''
        elif s[i] == "}":
            tem.add(int(num))
            dic[len(tem)] = tem
            num = ''
        elif s[i] == ",":
            if num != '':
                tem.add(int(num))
                num = ''
        else:
            num += s[i]
    cnt = max(dic.keys())
    answer = list(dic[1])
    for i in range(2, cnt + 1):
        a = dic[i] - set(answer)
        answer.append(list(a)[0])
    return answer