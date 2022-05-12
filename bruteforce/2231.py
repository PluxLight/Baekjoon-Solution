n = int(input())
answer = 0

for i in range(1, n):
    decom = sum(list(map(int, str(i))))
    if n == decom + i:
        answer = i
        break

print(answer)

# a = 215
# a = str(a)
# a = list(map(int, a))

# print(a)
