def solution(n, t, m, timetable):
    answer = 0
    # 버스는 9시부터 운영
    start = 9*60
    busTime = [start + t * i for i in range(n)]  # 버스 시간

    # 탑승시간을 분으 변경
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()

    # 탈 수 있는 버스중 가장 마지막 버스 탑승
    index = 0  # 버스에 탈 크루의 인덱스
    for bt in busTime:  # 버스 도착 시간을 순회하면서
        cnt = 0  # 버스에 탑승한 크루 수
        while cnt < m and index < len(timetable) and timetable[index] <= bt:
            index += 1
            cnt += 1
        if cnt < m:  # 버스에 자리 남았으면 버스타임에 내가 타면 됨
            answer = bt
        else:  # 버스에 탈 자리 없으면 맨 마지막 크루보다 1분전에 도착
            answer = timetable[index - 1] - 1

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)