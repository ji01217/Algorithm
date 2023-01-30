def solution(s):
    answer = ""
    lst = s.split(" ")
    for word in lst:
        cap = word.capitalize()
        answer += cap + " "
    return answer[:-1]