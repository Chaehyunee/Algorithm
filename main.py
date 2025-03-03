# 코딩 연습을 위한 Python 스크립트입니다.
# Ctrl+F5을(를) 눌러 실행
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
import time
start_time = time.time()
# 코드 시작

name_list = []
index_map = {}
N, M = map(int, input().split())

for n in range(N):
    name = input()
    name_list.append(name)
    index_map[name] = n + 1

for m in range(M):
    q = input()
    if q.isdigit():
        print(name_list[int(q)-1])
    else:
        print(index_map[q])

# 코드 끝
end_time = time.time()
print('time: ', end_time-start_time)
