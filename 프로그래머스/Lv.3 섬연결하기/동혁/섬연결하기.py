import heapq


def solution(n, costs):
    answer = 0
    li = [[-1] * n for _ in range(n)]
    bridge = [float('inf')] * n  # 가중치
    check = [-1] * n  # 방문여부

    # 그래프 인접 행렬 구성
    for i in costs:
        li[i[0]][i[1]] = i[2]
        li[i[1]][i[0]] = i[2]

    # 다익스트라 알고리즘 초기화
    bridge[0] = 0
    pq = [(0, 0)]  # (cost, node)

    while pq:
        current_cost, next_node = heapq.heappop(pq)

        #         방문하지 않은 노드 검사
        if check[next_node] != -1:
            continue

        #         현재 노드를 방문 처리
        check[next_node] = 1
        answer += current_cost

        for i in range(n):
            if li[next_node][i] != -1 and check[i] == -1:
                new_cost = li[next_node][i]
                if bridge[i] > new_cost:
                    bridge[i] = new_cost
                    heapq.heappush(pq, (new_cost, i))

    return answer
