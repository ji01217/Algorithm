def solution(arr1, arr2):
    answer = []
    M = len(arr1)
    N = len(arr2[0])
    K = len(arr2)
    for m in range(M):
        lst = []
        for n in range(N):
            a = 0
            for k in range(K):
                a += arr1[m][k] * arr2[k][n]
            lst.append(a)
        answer.append(lst)
    return answer