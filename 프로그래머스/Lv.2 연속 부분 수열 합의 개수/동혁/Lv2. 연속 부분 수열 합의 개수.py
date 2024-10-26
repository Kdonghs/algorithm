def solution(elements):
    answer = set()

    for i in range(1,len(elements)+1):
        for j in range(len(elements)-i+1):
            answer.add(sum(elements[j:j+i]))
        if i!=1:
            for j in range(i-1):
                answer.add(sum(elements[len(elements)-j-1:]) + sum(elements[:+i-j-1]))
    return len(answer)