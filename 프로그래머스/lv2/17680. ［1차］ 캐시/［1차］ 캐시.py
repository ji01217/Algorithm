def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        c = city.lower()
        if c in cache: # 캐시 적중
            cache.pop(cache.index(c))
            cache.append(c)
            answer += 1
        else: # 캐시 실패
            if len(cache) == cacheSize and cacheSize > 0:
                cache.pop(0)
            cache.append(c)
            answer += 5
    return answer