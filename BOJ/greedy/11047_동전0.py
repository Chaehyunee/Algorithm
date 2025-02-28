N, K = map(int, input().split()) # 코인 종류, 원하는 금액
coin = [] # 코인 종류를 저장할 리스트
cnt = 0 # 코인의 개수
for n in range(N):
    coin.append(int(input()))

for n in range(1, N+1): # 1부터 N까지 뒤에서부터 인덱싱
    if K % coin[-n] != K:
        cnt+= K // coin[-n]
        K %= coin[-n]

print(cnt)