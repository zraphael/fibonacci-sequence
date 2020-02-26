print('Fibonacci Sequence')

n = int(input('Number of terms you want to be shown:'))

n1 = 0
n2 = 1
print('-'*25)
print('{}'.format(n1))
print('{}'.format(n2))

count = 3
while count <= n:
    n3 = n1 + n2
    print('{}'.format(n3))
    count += 1
    n1 = n2
    n2 = n3
print('\n')