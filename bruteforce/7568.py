n = int(input())
humans = []
answer = []

for _ in range(n):
    wei, hei = map(int, input().split(' '))
    humans.append([wei, hei])

for human in humans:
    cnt = 1
    for other in humans:
        if human[0] < other[0] and human[1] < other[1]:
            cnt += 1
    answer.append(str(cnt))

print(' '.join(answer))
