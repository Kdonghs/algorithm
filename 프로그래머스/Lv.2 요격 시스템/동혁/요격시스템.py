def solution(targets):
    answer = 0
    end = -1
    targets.sort(key=lambda x: x[1])

    for targetStart, targetEnd in targets:
        if targetStart >= end:
            answer += 1
            end = targetEnd

    return answer
