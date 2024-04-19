from collections import defaultdict
from collections import deque


def solution(n, wires):
    answer = []

    # 에지 하나 씩 빼서 트리를 만들고 검사
    # 에지보다 노드가 하나더 많다
    for i in range(n - 1):
        dic = defaultdict(list)
        for m, j in enumerate(wires):
            if m == i:
                continue
            dic[j[0]].append(j[1])
            dic[j[1]].append(j[0])

        temp = int(countNode(dic, n))
        # 노드르 둘로 나누기 때문에 n,all-n으로 구성된다.
        # 작은 쪽에서 큰 쪽을 뺀다.
        answer.append(max(temp, n - temp) - min(temp, n - temp))

    return min(answer)


def countNode(dic, n):
    queue = deque([1])
    node = [0] * (n + 1)
    node[1] = 1

    while queue:
        temp = queue.popleft()
        for i in dic[temp]:
            if node[i] == 0:
                queue.append(i)
                node[i] = 1
    return node.count(1)
