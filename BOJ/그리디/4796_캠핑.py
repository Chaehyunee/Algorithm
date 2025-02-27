cnt=0
while True:
    l, p, v = map(int, input().split())
    cnt += 1
    if l==0 and p==0 and v==0: break #  연속 P일 중, L일 동안 사용 가능. V일 짜리 휴가
    num = (v // p) * l
    if l > (v%p): # 남은 날짜가 이용 가능 l일보다 크면
        num += v % p
    else:
        num += l
    print(f"Case {cnt}:", num)

