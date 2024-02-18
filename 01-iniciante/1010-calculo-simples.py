dados1 = input().split()
dados2 = input().split()

numero_peca1= int(dados1[1])
valor_peca1= float(dados1[2])

numero_peca2= int(dados2[1])
valor_peca2= float(dados2[2])



print("VALOR A PAGAR: R$ %.2f" %(numero_peca1*valor_peca1 + numero_peca2*valor_peca2))