
n = int(input())
humans = list(map(int, input().split()))
time = 0
humans.sort()
answer = 0

for human in humans:
    answer += human + time
    time += human





print(answer)
