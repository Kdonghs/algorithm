def solution(sticker):
    if len(sticker) == 1:
        return sticker.pop()

    size = len(sticker)

    #     1번 스티커부터 퐁당퐁당
    dp1 = [0] + sticker[:-1]
    for i in range(2, size):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

    #     2번 스티커부터 퐁당퐁당
    dp2 = [0] + sticker[1:]
    for i in range(2, size):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + dp2[i])

    print(dp1, dp2)
    return max(dp1[-1], dp2[-1])