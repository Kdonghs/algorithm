from collections import defaultdict

def solution(n, roads, sources, destination):
    dic = defaultdict(list)
    queue = [destination]
    visit = [-1] * (n + 1)
    visit[destination] = 0

    for i in roads:
        dic[i[1]].append(i[0])
        dic[i[0]].append(i[1])

    while queue:
        temp = queue.pop(0)

        for i in dic[temp]:
            if visit[i] == -1:
                visit[i] = visit[temp] + 1
                queue.append(i)

    return [visit[i] for i in sources]