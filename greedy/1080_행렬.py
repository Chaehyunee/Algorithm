N, M = map(int, input().split())

# A, B 입력받기
A=[list(map(int, list(input()))) for _ in range(N)]
B=[list(map(int, list(input()))) for _ in range(N)]


def get_same():
    cnt = 0  # 변경 횟수

    if N<3 or M<3: # 3x3보다 작은 경우
        return -1 if A!=B else 0

    # 모든 요소 비교
    for n in range(N - 2):
        for m in range(M - 2):
            if A[n][m] != B[n][m]: # 다른 것 발견
                for i in range(3):
                    for j in range(3):
                        A[n+i][m+j] = not A[n+i][m+j]
                cnt += 1


    return cnt if A==B else -1



print(get_same())