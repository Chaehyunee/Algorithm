N, M = map(int, input().split())
pack = [0]*M # 패키지 가격 리스트
one = [0]*M # 낱개 가격 리스트

for m in range(M):
    pack[m], one[m] = map(int, input().split())

pack_min = min(pack)
one_min = min(one)
if one_min*6 < pack_min: # 낱개로 사는게 저렴한 경우
    cnt = one_min*N
else:
    cnt = (N // 6) * pack_min  # 최종 가격
    if (N % 6)*one_min >= pack_min:
        cnt += pack_min
    else:
        cnt += (N % 6)*one_min

print(cnt)