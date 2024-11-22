def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    if 'B#' in music:
        music = music.replace('B#', 'b')
    return music


def solution(m, musicinfos):
    answer = []

    for n, info in enumerate(musicinfos):

        music = info.split(',')
        start = music[0].split(':')  # 시작 시간
        end = music[1].split(':')  # 종료 시간

        # 재생시간 계산
        time = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))

        changed = change(music[3])

        # 재생시간에 재생된 음
        b = changed * (time // len(changed)) + changed[:time % len(changed)]

        # 기억한 멜로디
        m = change(m)

        # 기억한 멜로디가 재생된 음에 있다면 결과배열에 [시간, index, 제목]을 추가
        if m in b:
            answer.append([time, n, music[2]])

    if not answer:
        return "(None)"
    # 결과배열의 크기가 1이라면 제목 리턴
    elif len(answer) == 1:
        return answer[0][2]
    # 결과 배열의 크기가 2보다 크다면 재생된 시간이 긴 음악, 먼저 입력된 음악순으로 정렬
    else:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2]  # 첫번째 제목을 리턴