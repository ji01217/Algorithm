def solution(n):
    ans = 0
    position = n
    while position >= 1:
        position, r = divmod(position, 2)
        ans += r
    return ans