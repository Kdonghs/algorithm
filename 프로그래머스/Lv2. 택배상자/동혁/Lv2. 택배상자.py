def solution(order):
    answer = 0
    temp = []
    input = 1
    for i in order:
        # 새 박스가 오더보다 작을 때
        while i > input:
            temp.append(input)
            input += 1

        #새 박스가 오더와 같을 때
        if input == i:
            input+=1
            answer+=1
            continue

        #창고에 존재하는지 확인
        if temp[-1]==i:
            temp.pop()
            answer+=1
            continue
        else:
            break

    return answer