fx = input().split(sep='-') # '-' 기준 분리
result = []

for x in fx:
    num = x.split(sep='+') # 분리된 str 을 다시 '+' 로 분리
    result.append(sum((int(n)*-1 for n in num))) #모든 숫자 음수화 시켜서 sum 후 저장
result[0] *= -1 # 맨 첫 숫자만 원래대로 돌리기
print(sum(result))