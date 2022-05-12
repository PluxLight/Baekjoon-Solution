n = int(input())
dt = list(map(int, input().split()))
costs = list(map(int, input().split()))

save_cost = costs[0]
answer = 0

for i in range(1, len(costs)):
    answer += save_cost * dt[i-1]
    if save_cost > costs[i]:        
        save_cost = costs[i]

print(answer)

"""
입력받은 비용 리스트를 반복문을 이용하여 일일이 살펴보는 방법을 사용했습니다.


반복문을 돌리기 전 첫번째 마을에서 최소 다음 마을로 갈 기름을 채워야 하기에 변수를 선언해 값을 저장해둡니다.


반복문에서는 먼저 비용 합계에 저장했던 비용과 거리를 곱하여 더해줍니다. 

그 후 도착한 마을의 비용이 저장한 비용보다 낮으면 값을 변경해줍니다. 그렇지 않으면 그대로 반복문을 계속 실행합니다.

이렇게 되면 초기 비용보다 값이 작은 마을이 나오기 전까지는 그 곳의 기름을 계속 사용하게 됩니다.
"""