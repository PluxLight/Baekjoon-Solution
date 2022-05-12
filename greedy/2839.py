import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

n = int(sys.stdin.readline())
three = 0
five = int(n/5)
n %= 5

while (five >= 0):
    if (n%3 == 0):
        three = int(n/3)
        n %= 3
        break
    five -= 1
    n += 5

print(five + three if n == 0 else -1)