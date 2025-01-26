def solution(n, info):
    res = []
    #     타겟, 발사 히스토리
    q = [(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    maxGap = 0

    #     0점 과녁부터 10점 과녁까지 발사
    while q:
        focus, arrow = q.pop(0)

        #         화살을 다 쏜 경우
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            #             라이언이 이기면
            if apeach < lion:
                gap = lion - apeach
                if maxGap > gap:
                    continue
                #                     기존 값을 초과해서 이기면
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                #                     발사 히스토리 저장
                res.append(arrow)  # 최대점수차를 내는 화살상황 저장

        #          화살 더 쏜 경우
        elif sum(arrow) > n:
            continue

        #          화살 덜 쏜 경우
        elif focus == 10:
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))

        #          화살 쏘기
        #          어피치가 쏜 화살보다 1발 더 많아야 함
        else:
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))  # focus과녁에 발사 하기

            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))  # focus과녁에 발사 안하기

    #     초과해서 성적을 낸적이 없는 경우
    if not res:
        return [-1]
    else:
        return res[-1]