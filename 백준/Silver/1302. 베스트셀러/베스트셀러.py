# 입력
N = int(input())
lst = []
st = set()
for _ in range(N):
    book = input()
    lst.append(book)
    st.add(book)

# 풀이
ans = 0
ans_title = []
for i in st:
    cnt = lst.count(i)
    if cnt > ans:
        ans = cnt
        ans_title = [i]
    elif cnt == ans:
        ans_title.append(i)

# 출력
ans_title.sort()
print(ans_title[0])