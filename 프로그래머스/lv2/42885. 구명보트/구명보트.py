def solution(people, limit):
    answer = len(people)
    i = 0
    people.sort(reverse=True)
    while i <= len(people) - 2:
        if people[i] + people[-1] <= limit:
            people.pop()
            answer -= 1
        i += 1
    return answer