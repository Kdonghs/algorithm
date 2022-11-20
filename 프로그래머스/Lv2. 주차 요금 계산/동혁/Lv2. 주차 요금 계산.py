import math
from collections import defaultdict

def solution(fees, records):
    temp = defaultdict(int)
    last = 23*60+59
    stack = {}
    answer=[]

    for i in records:
        time,num,io = i.split()
        if io == "IN":
            stack[num]=time
        else:
            oh,om=time.split(':')
            ih,im = stack.pop(num).split(":")

            m = (int(oh) - int(ih))*60 - int(im) + int(om)
            temp[int(num)]+=m

    for i in stack:
        oh, om = stack[i].split(':')
        m = last - int(oh) * 60 - int(om)
        temp[int(i)]+=m
    temp = sorted(temp.items())

    for i in temp:
        fee = fees[1]
        if i[1] > fees[0]:
            fee += math.ceil((i[1] - fees[0]) / fees[2]) * fees[3]

        answer.append(fee)

    return answer