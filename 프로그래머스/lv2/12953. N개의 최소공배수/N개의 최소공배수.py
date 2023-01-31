def solution(arr):
    a = 1
    for i in arr:
        a *= i
    arr.sort(reverse=True)
    for i in range(arr[0], a):
        for j in arr:
            if i % j != 0:
                break
            if j == arr[-1]:
                return i
    return a