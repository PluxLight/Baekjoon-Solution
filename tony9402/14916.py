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