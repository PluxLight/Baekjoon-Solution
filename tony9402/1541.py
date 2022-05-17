# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호

formulas = input().split('-')
answer = 0

for formula in formulas[0].split('+'):
    answer += int(formula)

for formula in formulas[1:]:
    for f in formula.split('+'):
        answer -= int(f)

print(answer)

"""
-가 있는 경우에는 첫 -가 나오기 전 값들을 전부 더해줍니다.

그리고 - 이후의 값들은 더해진 값들을 계속 뺄셈해주면

가장 작은 값을 만들 수 있습니다.


-가 없다면 값들을 전부 더해주어야 합니다.
"""