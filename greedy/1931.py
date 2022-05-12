n = int(input())
meetings = []
start = 0
end = 0
answer = 0

for _ in range(n):
    meetings.append(list(map(int, input().split())))


meetings = sorted(meetings, key = lambda x : [x[1], x[0]])

for meet in meetings:
    if end <= meet[0]:
        start = meet[0]
        end = meet[1]
        answer += 1


print(answer)