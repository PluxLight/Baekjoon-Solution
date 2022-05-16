def main():
	t = int(input())

	for i in range(t):
		list_t = list(map(int, input().split()))
		# 0 == l, 1 == s, 2 == n, 3 == k, 4 == m, 5... = v
		if list_t[2] < list_t[1]/list_t[0] * 100:
			return 0
		for j in list_t[5:]:
			if j <= list_t[4]:
				return 0	
		
	return 1
		
		
		
print(main())