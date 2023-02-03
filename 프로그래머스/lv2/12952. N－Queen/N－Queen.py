def nqueen(queen, n, row):
    count = 0
    
    if n == row:
        return 1
    
    # 가로로 한번만 진행
    for col in range(n):
        queen[row] = col
        
        # 앞의 것과 비교
        for x in range(row):
            if queen[x] == queen[row]:
                break
            if abs(queen[x]-queen[row]) == row-x:
                break
        else:
            count += nqueen(queen, n, row+1)
    return count

def solution(n):
    queen = [0] * n
    return nqueen(queen, n, 0)