def solution(numbers):
    answer = []
    for i in numbers:
        # 2진수로 치환
        li = list('0'+bin(i)[2:])
        # 낮은 비트를 1로 바꿀수록 원래 숫자와 가까워짐
        idx = ''.join(li).rfind('0')
        li[idx]='1'

        # 자리 올림 고려
        if i%2==1:
            li[idx+1]='0'
        answer.append(int(''.join(li),2))
    return answer