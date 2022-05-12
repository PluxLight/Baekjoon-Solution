def calc_as(i):
    num = str(i)
    num = list(map(int, num))
    dif = num[0] - num[1]

    for i in range(1, len(num) - 1):
        if dif != num[i] - num[i+1]:
            return 0

    return 1


n = int(input()) + 1
answer = 0

for i in range(1, n):
    if i < 100:
        answer += 1
    else:
        answer += calc_as(i)

print(answer)
