def solution(cacheSize, cities):
    answer = 0
    cash = [0] * cacheSize

    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for i in cities:
            # 모든 문자는 대문자로 치환해서 비교
            city = i.upper()

            # 캐시에 들어있으면 1초
            # 가장 마지막에 참조 했으므로 가장 마지막에 올려 놓는다.
            if city in cash:
                cash.remove(city)
                cash.append(city)
                answer += 1

            # 캐시에 없으면 5초
            # 가장 마지막에 참조된 캐시를 삭제(LRU)하고 마지막 캐시에 새로운 도시 추가
            else:
                cash.pop(0)
                cash.append(city)
                answer += 5
    return answer
enumerate