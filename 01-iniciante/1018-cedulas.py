valor = int(input())
notas_cem = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
notas_1 = 0

print(valor)
if(valor >= 100):
    notas_cem = int(valor / 100)
    valor = valor - notas_cem*100

print("%i nota(s) de R$ 100,00" %notas_cem)

if(valor >= 50):
    notas_50 = int(valor / 50)
    valor = valor - notas_50*50

print("%i nota(s) de R$ 50,00" %notas_50)

if(valor >= 20):
    notas_20 = int(valor / 20)
    valor = valor - notas_20*20

print("%i nota(s) de R$ 20,00" %notas_20)

if(valor >= 10):
    notas_10 = int(valor / 10)
    valor = valor - notas_10*10

print("%i nota(s) de R$ 10,00" %notas_10)

if(valor >= 5):
    notas_5 = int(valor / 5)
    valor = valor - notas_5*5

print("%i nota(s) de R$ 5,00" %notas_5)

if(valor >= 2):
    notas_2 = int(valor / 2)
    valor = valor - notas_2*2

print("%i nota(s) de R$ 2,00" %notas_2)

if(valor >= 1):
    notas_1 = int(valor / 1)
    valor = valor - notas_1*1

print("%i nota(s) de R$ 1,00" %notas_1)

