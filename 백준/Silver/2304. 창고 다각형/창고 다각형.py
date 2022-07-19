# 입력
maxH = 1  # 가장 높은 기둥의 높이
maxL = 0  # 마지막 기둥의 왼쪽 면
N = int(input())
pillar = []
# maxH, maxL 찾기
for i in range(N):
    L, H = map(int, input().split())
    pillar.append([L, H])
    if maxL < L:
        maxL = L
    if maxH < H:
        maxH = H
        maxIndex = L


# 풀이
pillarList = [0] * (maxL + 1)
for l, h in pillar:
    pillarList[l] = h

total = 0  # 총 기둥 높이 == 다각형 면적
temp = 0  # 현재 기둥 높이
for i in range(maxIndex + 1):  # 맨앞부터 가장 높은 기둥까지
    if pillarList[i] > temp:  # 기존 기둥 높이보다 현재위치 기둥이 높으면 temp 기둥 높이를 높인다.
        temp = pillarList[i]
    total += temp
temp = 0  # 현재 기둥 높이 초기화
for i in range(maxL, maxIndex, -1):  # 맨뒤에서 가장 높은 기둥 전까지 (오목한 부분이 있으면 안되므로 반대로)
    if pillarList[i] > temp:
        temp = pillarList[i]
    total += temp

# 출력
print(total)