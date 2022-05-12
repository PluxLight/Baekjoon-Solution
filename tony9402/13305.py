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