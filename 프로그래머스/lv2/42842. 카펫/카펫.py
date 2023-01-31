def solution(brown, yellow):
    width, height = 0, 0
    border = brown//2 + 2
    for i in range(border//2 + 1):
        if i * (border - i) == brown + yellow:
            width = border - i
            height = i
    return [width, height]