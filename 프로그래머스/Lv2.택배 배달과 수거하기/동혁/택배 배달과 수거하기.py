def solution(cap, n, deliveries, pickups):
    answer = 0
    # 마지막부터 검사
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    deli = 0
    pick = 0

    for i in range(n):
        # 픽업하거나 배달해야할 물건 탐색
        deli += deliveries[i]
        pick += pickups[i]

        # 픽업하거나 배달해야할 물건 용량 탐색
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap

            # 왕복이므로2배, 역순이므로 n-i
            answer += (n - i) * 2

    return answer