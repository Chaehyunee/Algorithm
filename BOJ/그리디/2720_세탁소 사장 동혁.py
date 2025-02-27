# T 로 테스트 케이스 개수 입력 받기
T = int(input())
coin_types = [25, 10, 5, 1] # q, d, n, p

def get_charge():
    C = int(input())
    counts = [0]*4
    for i in range(len(counts)):
        counts[i] = C//coin_types[i]
        C %= coin_types[i]

    print(*counts)


for t in range(T):
    get_charge()
