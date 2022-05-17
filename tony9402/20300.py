# https://www.acmicpc.net/problem/20300
# 서강근육맨

n = int(input())

equipments = list(map(int, input().split()))
answer = 0
equipments.sort()

if n%2 == 1:
    point = 2
else:
    point = 1

for i in range(n//2):
        answer = max(answer, equipments[i] + equipments[-i-point])

print(answer)

"""
입력 받은 장비들을 정렬해 줍니다

가장 작은 값과 가장 큰 값을 합쳐줍니다 그리고 그 다음 작은 값과 큰 값을 합치고 이를 계속 비교해줍니다

비교한 값들 중 가장 큰 값이 정답이므로 이를 출력합니다

만약 입력 받은 장비의 수가 홀수면 가장 큰 값을 제외하고 아니면 그대로 진행합니다.


"""