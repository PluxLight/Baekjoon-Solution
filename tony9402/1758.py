n = int(input())
answer = 0
tips = []

for _ in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)

for i, tip in enumerate(tips):
    now_tip = tip - i
    if now_tip > 0:
        answer += now_tip
    else:
        break

print(answer)