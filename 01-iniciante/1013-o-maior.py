entrada = input().split()

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maiorab = (a + b + abs(a-b)) /2
maiorbc = (maiorab + c + abs(maiorab-c)) /2


print("%i eh o maior" %maiorbc)