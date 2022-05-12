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


"""
팁의 값이 큰 순서로 배치하면 가장 이득을 많이 볼 수 있을거라 생각하여 입력 받은 후 내림차순 정렬을 했습니다.


그 후 문제가 제시한 조건대로 팁을 계산해 더해주었습니다. 

내림차순 정렬을 했으니 계산한 팁이 한 번 0 이하가 되면 그 이후로도 0이 될테니 더 계산해 줄 필요가 없습니다. 

그러므로 계산한 값이 0 이하가 되면 반복문을 종료합니다.

"""