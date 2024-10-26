def solution(s):
    answer = []
    count = 0
    zero = 0
    enumerate
    while s!='1':
        count+=1

        zero+= s.count('0')
        s=s.replace('0','')
        s = format(len(s),'b')
        print(s)

    answer = [count,zero]
    return answer