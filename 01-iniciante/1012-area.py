entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

pi = 3.14159

triangulo = (a * c) /2
circulo = c**2 * pi
trapezio = (a+b) *c /2
quadrado = b*b
retangulo = a*b

print("TRIANGULO: %.3f" %triangulo)
print("CIRCULO: %.3f" %circulo)
print("TRAPEZIO: %.3f" %trapezio)
print("QUADRADO: %.3f" %quadrado)
print("RETANGULO: %.3f" %retangulo)