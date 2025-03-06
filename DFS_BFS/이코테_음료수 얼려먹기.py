N, M = map(int, input().split())
ice = []
cnt = 0
dm = [0, 0, -1, 1]
dn = [-1, 1, 0, 0]

for n in range(N):
    ice.append(list(map(int, input())))

def dfs(ice, cn, cm):
    # 범위 벗어나면 기각
    if cn < 0 or cm < 0 or cn > N-1 or cm > M-1:
        return False
    if not ice[cn][cm]: #현재 자리가 0이면
        ice[cn][cm]=1 #현재 위치 방문 처리 (구멍 메우기)
        # 주변 탐색
        for i in range(len(dm)):
            dfs(ice, cn+dn[i], cm+dm[i]) # 상, 하, 좌, 우 호출
        return True
    return False


for n in range(N):
    for m in range(M):
        if dfs(ice, n, m):
            cnt += 1

print(cnt)