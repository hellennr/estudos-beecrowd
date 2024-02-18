tempo = int(input())

hora = 60*60
minuto = 60
qnt_hora =0
qnt_min = 0

if(tempo >= hora):
    qnt_hora= int(tempo / hora)
    tempo = tempo - qnt_hora * hora
    
if(tempo >= minuto):
    qnt_min = int(tempo/minuto)
    tempo = tempo - qnt_min * minuto



print("%i:%i:%i" %(qnt_hora,qnt_min,tempo))