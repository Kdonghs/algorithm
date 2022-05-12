number = [1,1,1,1,1]
target = 3

def dfs(numbers,target,depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += dfs(numbers,target,depth+1)
        numbers[depth] *= -1
        answer += dfs(numbers,target,depth+1)
    return answer

def a(numbers, target):
    answer = 0
    return dfs(numbers,target,0)

print(a(number,target))
