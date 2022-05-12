def generator_num(i, gene_nums):
    while i:
        gene_num = sum(list(map(int, str(i)))) + i
        if gene_num <= 10000 and gene_nums[gene_num] == 0:
            gene_nums[gene_num] = 1
            i = gene_num
        else:
            return
            


gene_nums = [0 for _ in range(10001)]
gene_nums[0] = 1

# print(gene_num)

for i in range(1, 10001):
    if gene_nums[i] == 0:
        generator_num(i, gene_nums)
        
for i,j in enumerate(gene_nums):
    if j == 0:
        print(i)









"""
n = int(input())
answer = 0

for i in range(1, n):
    decom = sum(list(map(int, str(i))))
    if n == decom + i:
        answer = i
        break

print(answer)
"""