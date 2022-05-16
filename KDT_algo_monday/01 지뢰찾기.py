dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

n, m = map(int, input().split())
arr = []

for _ in range(m):
	arr.append(list(map(str, input())))
	
# print(arr)

for i in range(m): # i, m값이 세로
	for j in range(n): # j, n값이 가로
		if arr[i][j] == '*':
			continue
		else:
			cnt = 0
			for k in range(8):
				x = j + dx[k]
				y = i + dy[k]
				if 0 <= x < n and 0 <= y < m and arr[y][x] == '*':
					cnt += 1
					
			arr[i][j] = cnt
			
for a in arr:
	print("".join(map(str, a)))