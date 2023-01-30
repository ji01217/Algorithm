def solution(n):
    Fibo = [0, 1]
    index = 1
    while index <= n:
        value = Fibo[index] + Fibo[index-1]
        if value >= 1234567:
            value %= 1234567
        Fibo.append(value)
        index += 1
    return Fibo[n]