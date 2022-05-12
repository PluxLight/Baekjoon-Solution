def main():
    n = int(input())
    money = n // 5

    if n % 5 == 0: return money # 5원으로만 거슬러 줄 수 있으면 리턴

    change = n % 5

    while money >= 0:
        if change % 2 == 0:
            return money + change // 2
        money -= 1
        change += 5

    return -1


print(main())


"""
2839번 설탕배달과 비슷하게 구현하여 풀이했습니다.


먼저 가장 큰 수인 5로 나눈 후, 나누어 떨어지면 그대로 값을 리턴합니다.


5로 나누어 떨어지지 않으면 아래 작업을 반복합니다.

5로 나누었던 나머지 값들을 2로 나누어 떨어지는지 확인하고 나누어 떨어진다면 5로 나눈 몫과 2로 나눈 몫을 합쳐 리턴합니다.

조건을 만족하지 않으면 5로 나눈 값을 하나 줄이고 나머지 값을 5만큼 늘려줍니다.


5로 나눈 몫이 0 미만이 되면 거스름돈을 5와 2로 줄 수 없는 경우가 되므로 반복문을 빠져나와 -1을 리턴합니다.
"""