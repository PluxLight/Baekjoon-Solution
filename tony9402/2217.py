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