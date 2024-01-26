def solution(k, tangerine):
    answer = 0

    # 각각의 귤을 딕셔너리 형태로 치환
    li = {}
    for i in tangerine:
        if i in li:
            li[i] += 1
        else:
            li[i] = 1
    # 귤이 많은 순서로 정렬
    li = dict(sorted(li.items(), key=lambda x: x[1], reverse=True))

    # 많은 순서대로 귤 선택
    for i in li:
        if k <= 0:
            return answer
        k -= li[i]
        answer += 1
    return answer