from collections import deque
import copy

# TODO DFS stack 버전 만들기
# Stack 이용
# def dfs(graph, v):
#     # 시작 노드 stack 삽입
#     stack = [v]
#     # 시작 노드 방문 처리
#     print(v, end=' ')
#     cnt = 0
#     while cnt < m:
#         print('stack: ', stack)
#         # 인접 노드가 있는지 확인
#         if len(graph[v]) > 1:
#             # 인접 노드 중 stack에 없는 것 중에 최소 노드
#             c_node = min(set(stack)-set(graph[v]))
#             # 스택 삽입
#             stack.append(c_node)
#             # 현재 노드 방문 처리
#             print(c_node, end=' ')
#             # 방문한 노드 graph 에서 지우기
#             graph[v].remove(c_node)
#             graph[c_node].remove(v)
#         else: # 인접 노드가 없으면 pop
#             stack.pop()
#         v = stack[-1]
#         cnt += 1







# Queue 이용
from collections import deque

bfs_result=[]
dfs_result=[]

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    dfs_result.append(v)
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# BFS 메서드 정의
def bfs(graph, start, visited):
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        bfs_result.append(v)
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# n: 정점의 개수 m: 간선의 개수 v: 시작 정점
n, m, v = map(int, input().split())

# 그래프 리스트
graph = [[] for _ in range(n+1)]

# visited list
dfs_visited = [False]*(n+1)
bfs_visited = [False]*(n+1)

# 간선 입력
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 그래프 내 node 작은 것부터
for i in range(n+1):
    graph[i].sort()

print(graph)
dfs(graph, v, dfs_visited)
bfs(graph, v, bfs_visited)

print(*dfs_result, sep=' ')
print(*bfs_result, sep=' ')