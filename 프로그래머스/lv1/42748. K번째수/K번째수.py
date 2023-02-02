def solution(array, commands):
    answer = []
    cnt = len(commands)
    for c in range(cnt):
        i, j, k = commands[c]
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])
    return answer