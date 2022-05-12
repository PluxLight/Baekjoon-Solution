def main():
    n = input()

    n = n.replace('XXXX', 'AAAA')
    n = n.replace('XX', 'BB')

    if 'X' in n:
        return -1
    
    return n


print(main())



# n = 'XX.XXXXXXXXXX..XXXXXXXX...XXXXXX'

# n = n.replace('XXXX', 'AAAA')
# n = n.replace('XX', 'BB')
# print(n)