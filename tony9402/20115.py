# https://www.acmicpc.net/problem/20115

# 20115번 에너지 드링크

# n = int(input())
# drinks = list(map(int, input().split()))

# drinks.sort(reverse=True)
# answer = drinks[0]/2

# for drink in drinks:
#     answer += drink/2

# print(answer)

"""
문제에서 제시한 방식대로 가장 큰 값을 만들기 위해서 입력 받은 값들을 내림차순 해줍니다.

가장 큰 값은 그대로 유지되고 나머지 값들은 반으로 나뉘어져 합계를 구하게 됩니다.

"""

"""
n = int(input())
drinks = list(map(int, input().split()))
drinks = list(map(lambda x: x/2, drinks))

answer = sum(drinks) + max(drinks)

print(answer)
"""