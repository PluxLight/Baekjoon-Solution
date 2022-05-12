n = int(input())
answer = 0
ropes = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort()
cnt = n

for rope in ropes:
    if rope * cnt > answer:
        answer = rope * cnt
    cnt -= 1

print(answer)


"""
로프가 견딜 수 있는 중량이 (버틸 수 있는 가장 작은 중량) * (로프의 수) 이므로 입력 받은 로프들을 정렬해 줍니다. (오름차순)

그 후 로프의 수를 하나씩 줄이며 곱한 로프의 값 중 가장 큰 값을 출력해줍니다
"""