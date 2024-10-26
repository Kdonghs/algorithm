def solution(scores):
    #     1등부터 밀림
    answer = 1

    wanho = scores[0]
    total = sum(wanho)
    #     근태 내림차순, 동료평가 오름차순
    scores.sort(key=lambda x: (-x[0], x[1]))

    peer = 0
    for i in scores:
        #         완호의 평가가 상대적으로 모두 낮다면 인센티브를 받을 수 없다.
        if wanho[0] < i[0] and wanho[1] < i[1]:
            return -1
        #         직전 사람보다 동료평가의 점수가 크다면 순위가 밀릴 여지가 있음
        if peer <= i[1]:
            #         토탈 점수가 밀린다면 등수도 밀림
            if total < i[0] + i[1]:
                answer += 1
            peer = i[1]
    return answer