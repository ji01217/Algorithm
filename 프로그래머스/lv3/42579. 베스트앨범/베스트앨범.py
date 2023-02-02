def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}
    cnt = len(genres)
    for i in range(cnt):
        genre = genres[i]
        if genre in dic1.keys():
            dic1[genre] += plays[i]
            dic2[genre].append((i, plays[i]))
        else:
            dic1[genre] = plays[i]
            dic2[genre] = [(i, plays[i])]
    sort_genres = sorted(dic1.items(), key = lambda x: -x[1])
    for i in range(len(sort_genres)):
        genre = sort_genres[i][0]
        lst = sorted(dic2[genre], key = lambda x: -x[1])
        answer.append(lst[0][0])
        if len(lst) >= 2:
            answer.append(lst[1][0])
    return answer