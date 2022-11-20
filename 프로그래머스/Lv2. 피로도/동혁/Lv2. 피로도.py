from itertools import permutations

def solution(k, dungeons):
    answer = 0
    num = len(dungeons)
    for i in permutations(dungeons,num):
        hp = k
        count = 0
        for j in i:
            if hp>= j[0]:
                count+=1
                hp-=j[1]
            else:
                break
        if answer < count:
            answer=count

    return answer