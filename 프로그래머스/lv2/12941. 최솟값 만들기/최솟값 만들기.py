def solution(A,B):
    answer = 0
    length = len(A)
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer