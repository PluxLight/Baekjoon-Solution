def main():
    n = input()

    n = n.replace('XXXX', 'AAAA')
    n = n.replace('XX', 'BB')

    if 'X' in n:
        return -1
    
    return n


print(main())


"""
Python의 replace를 이용하여 풀었습니다

replace 작업 후 X가 남아있으면 -1을 리턴하고 그렇지 않으면 변환한 n을 리턴합니다

.

.

.

replace를 사용하지 않고 풀이한다면

for 반복문으로 [i : i+4]로 입력받은 문자열을 확인하여 조건에 맞으면 AAAA로 변환

마찬가지로 [i : i+2]로 입력받은 문자열을 확인하여 조건에 맞으면 BB로 변환 후

X가 남아있으면 -1 그렇지 않으면 변환한 문자열을 리턴
"""




# n = 'XX.XXXXXXXXXX..XXXXXXXX...XXXXXX'

# n = n.replace('XXXX', 'AAAA')
# n = n.replace('XX', 'BB')
# print(n)

