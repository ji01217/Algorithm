import math

def solution(progresses, speeds):
    answer = []
    cnt = len(progresses)
    days = []
    for i in range(cnt):
        day = (100 - progresses[i]) / speeds[i]
        days.append(math.ceil(day))
    now_day = days[0]
    now_cnt = 1
    print(days)
    for i in range(1, cnt):
        if now_day < days[i]:
            answer.append(now_cnt)
            now_day = days[i]
            now_cnt = 1
        else:
            now_cnt += 1
    answer.append(now_cnt)
            
    return answer