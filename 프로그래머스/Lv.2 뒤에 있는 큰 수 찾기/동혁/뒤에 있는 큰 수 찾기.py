# ex)[2, 3, 3, 5]
# index 0 1 2 3
# value 2 3 3 5

# stack=[],answer=[-1,-1,-1,-1]
# stack=[0],answer=[-1,-1,-1,-1]
# stack=[1],answer=[3,-1,-1,-1]
# stack=[1,2],answer=[3,-1,-1,-1]
# stack=[1],answer=[3,-1,5,-1]
# stack=[],answer=[3,5,5,-1]
# stack=[3],answer=[3,5,5,-1]
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for n, i in enumerate(numbers):
        #         스택에 값이 존재하고 현재 숫자가 더 크다면
        #         현재의 값이 결과가 된다.
        while stack and numbers[stack[-1]] < i:
            answer[stack.pop()] = i
        stack.append(n)

    return answer