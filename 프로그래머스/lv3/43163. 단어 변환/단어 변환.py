from collections import deque

def solution(begin, target, words):
    answer = 0
    dic = {begin:0, target:0}
    for word in words:
        dic[word] = 0
    queue = deque()
    queue.append(begin)
    while queue:
        a = queue.popleft()
        for word in words:
            if dic[word] >= 1:
                continue
            cnt = 0
            for i in range(len(begin)):
                if a[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                dic[word] = dic[a] + 1
                queue.append(word)
    return dic[target]