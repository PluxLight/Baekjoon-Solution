n, k = map(int, input().split())
ans = 0

money = []

for _ in range(n):
    money.append(int(input()))

money.reverse()

for i in money:
    ans += k//i
    k = k%i

print(ans)