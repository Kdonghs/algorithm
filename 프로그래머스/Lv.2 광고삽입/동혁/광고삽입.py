# 시분초2초
def timeChange(t):
    result = []
    for i in t.split("-"):
        temp = list(map(int, i.split(":")))
        result.append(temp[0] * 60 * 60 + temp[1] * 60 + temp[2])

    return result

# 초2시간분초
def sec_to_time(sec):
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return f'{h:02}:{m:02}:{s:02}'


def solution(play_time, adv_time, logs):
    answer = sec_to_time(0)
    play = timeChange(play_time)[0]
    adv = timeChange(adv_time)[0]
    dp = [0] * (play + 1)

    #     각 범위 마킹
    for i in logs:
        s, e = timeChange(i)
        dp[s] += 1
        dp[e] -= 1

    #     누적합
    for i in range(1, play + 1):
        dp[i] += dp[i - 1]

    # 시작부터 광고길이까지 한칸씩 이동하며 비교
    left = 0
    MAX = total = sum(dp[:adv])
    for t in range(adv, play + 1):
        total -= dp[left]
        total += dp[t]
        left += 1
        # 기존보다 시청 시간이 더 길다면 시작 시간 변경
        if total > MAX:
            answer = sec_to_time(left)
            MAX = total

    return answer