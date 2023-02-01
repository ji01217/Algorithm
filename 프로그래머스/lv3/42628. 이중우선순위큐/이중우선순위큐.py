def solution(operations):
    answer = []
    queue = []
    for op in operations:
        if op == "D -1":
            if queue:
                queue.pop(0)
        elif op == "D 1":
            if queue:
                queue.pop()
        else:
            i, num = op.split()
            queue.append(int(num))
            queue.sort()
    if queue:
        answer = [max(queue), min(queue)]
    else:
        answer = [0, 0]
    return answer