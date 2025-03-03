# N 입력
N = int(input())

# LRUD 입력
command = list(input().split())
x, y = 1, 1

for c in command:
    if c == 'L' and y > 2: y-=1
    elif c == 'R' and y < N: y+=1
    elif c == 'U' and x > 2: x-=1
    elif c == 'D' and x < N: x+=1

print(x, y)


"""아래는 공식 답"""

# N을 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1] #x에 대한 방향값
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx = x + dx[i] #다음 칸 미리 계산
            ny = y + dy[i]
    #공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx > n or ny > n:
        continue

    # 이동 수행
    x, y = nx, ny

print(x, y)