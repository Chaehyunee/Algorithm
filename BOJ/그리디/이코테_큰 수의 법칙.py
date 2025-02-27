# 주어진 수들을 M 번 더하여 가장 큰 수 만들기
# 배열의 특정 인덱스의 수가 연속해서 K번 초과해 더해질 수 없음 (최대 K번)
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속덧셈 최대 횟수 K (K <= M)
# 2 <= N <= 1,000, 1 <= M <= 10,000, 1 <= K <= 10,000

N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
results, idx, k, m = 0, 0, 0, 0

while m < M: # m이 M번이 될 때까지
    results += num_list[idx] # 정렬된 리스트 제일 큰 값 선택
    m += 1 # 덧셈 횟수
    if idx > 0: idx, k = 0, 0 # idx가 0이 아니면, 다시 0으로 컴백
    k += 1
    if k >= K: idx += 1

print(results)




# 예시 답안
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 가장 작은 수

result = 0

while True:
    for i in range(k): # 가장 큰 수 k 번 더하기
        if m == 0: break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m==0: break # m이 0이라면 반복문 탈출
    result += second # 두번째로 큰 수 한번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

    print(result)

"""
문제의 요지: 가장 큰 수를 K번 더하고, 두 번째로 큰 수를 한 번 더하는 연산 을 반복 하기
핵심 식: int(M / (K+1)) * K + M % (K+1)
가져갈 생각: m번 더해야 끝난다 -> while True 문에서 m -=1 로 진행
반성: 내가 쓴 코드는 요지를 파악하지 못함. 계산 복잡도가 높음.
"""

572384-324327