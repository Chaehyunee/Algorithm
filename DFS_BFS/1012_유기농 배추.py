dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def find_min(cx, cy):
    # 현재 위치가 범위를 벗어나면 스킵
    if cx < 0 or cy < 0 or cx > M-1 or cy > N-1:
        return False

    # 배추가 있다!
    if cabbage[cy][cx]:
        cabbage[cy][cx] = 0 # 현재 위치를 방문 처리

        # 상하좌우에도 배추가 있다면
        for i in range(len(dx)):
            find_min(cx + dx[i], cy + dy[i])
        return True # 배추가 하나라도 있으면 True 인 것
    return False


T = int(input()) # 테스트케이스
for t in range(T):

    # NxM 에 심어진 K개 배추
    M, N, K = map(int, input().split())
    cabbage = [[0 for m in range(M)] for _ in range(N)]

    # 배추 위치 입력
    for k in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1

    cnt = 0
    # 최소 개수 세기
    for cx in range(M):
        for cy in range(N):
            if find_min(cx, cy): # 현재 위치에서 dfs 수행
                cnt += 1

    print(cnt)