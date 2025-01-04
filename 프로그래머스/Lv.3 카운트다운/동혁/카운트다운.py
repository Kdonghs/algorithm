def solution(target):
    darts = [100001] * 100001
    sb_count = [0] * 100001
    dic = {}

    for i in range(1, 21):
        dic[i * 2] = 0
        dic[i * 3] = 0
    for i in range(1, 21):
        dic[i] = 1
    dic[50] = 1

    #    한번에 맞출 수 있는 값들을 업데이트
    for i, j in dic.items():
        darts[i] = 1
        sb_count[i] = j

    #     나머지 업데이트
    for i in range(1, target + 1):
        #         이미 맞춘 값들은 패스
        if darts[i] != 100001:
            continue

        d = 100001
        sb = 0
        for score, _sb in dic.items():
            s = i - score
            #             버스트
            if s < 0:
                continue

            #           어느 다트만큼 뺀 점수가 한번도 업데이트 되지 못한 값이거나
            #           더 적은 횟수로 점수를 만들 수 있으면서 싱글과 불을 더 포함할 수 있으면 업데이트
            if (darts[s] + 1 < d) or (darts[s] + 1 == d and sb_count[s] + _sb > sb):
                d = darts[s] + 1
                sb = sb_count[s] + _sb

        darts[i] = d
        sb_count[i] = sb
    return [darts[target], sb_count[target]]