from itertools import combinations

n ,m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

for card in combinations(cards, 3):
    if sum(card) <= m:
        answer = max(sum(card), answer)

print(answer)