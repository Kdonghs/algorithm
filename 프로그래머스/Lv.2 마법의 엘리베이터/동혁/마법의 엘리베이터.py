def solution(storey):
    answer = 0

    # 각 자리수가 0이 되도록 맞춘다.
    # 26->27->28->29->30
    # 30->20->10->10
    while storey:
        temp = storey % 10

        if temp > 5:
            answer += (10 - temp)
            storey += 10
        elif temp < 5:
            answer += temp
        # 다음 자릿수를 확인해서 방향을 정함
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += temp

        storey //= 10
    return answer