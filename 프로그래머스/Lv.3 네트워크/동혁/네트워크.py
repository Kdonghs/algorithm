def BFS(n, computers, com, visited):
    #     현재 노드 방문 처리
    visited[com] = True
    queue = []
    #     현재 노드를 기준으로 탐색
    queue.append(com)

    while len(queue) != 0:
        com = queue.pop(0)
        #         이동한 노드의 방문 처리
        visited[com] = True

        #         갈 수 있는 노드를 큐에 추가
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)


def solution(n, computers):
    answer = 0
    #     방문 여부 확인하는 맵
    visited = [False for i in range(n)]

    #     각 노드별로 순회
    for com in range(n):
        #         방문을 않했다면 간선 추가
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
    return answer