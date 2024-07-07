def solution(begin, target, words):
    answer = 0
    queue = [[begin, 0]]
    visited = set()

    while queue:
        temp = queue.pop()
        if temp[0] == target:
            return temp[1]

        for i in 'abcdefghijklmnopqrstuvwxyz':
            for j in range(len(temp[0])):
                newWord = temp[0][:j] + i + temp[0][j + 1:]
                if newWord in words and newWord not in visited:
                    visited.add(newWord)
                    queue.append((newWord, temp[1] + 1))
    return 0