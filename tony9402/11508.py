n = int(input())
lactoses = []
answer = 0

for _ in range(n):
    lactoses.append(int(input()))

lactoses.sort(reverse=True)

for i in range(0, len(lactoses), 3):
    if i+3 <= n:
        answer += sum(lactoses[i:i+3]) - min(lactoses[i:i+3])
    else:
        answer += sum(lactoses[i:])
        break

print(answer)



"""
1758 알바생 경호와 비슷한 원리로 풀었습니다.

3개 제품 묶음 중 가장 저렴한 제품값 만큼 지불하지 않아도 되니 입력받은 값들을 내림차순 정렬해줍니다.

이후 반복문을 돌며 (3개 묶음 합) - (가장 저렴한 제품 값) 을 해줍니다.

3개 묶음이 안되면 남은 제품 가격을 전부 합치고 반복문을 빠져나옵니다.

"""