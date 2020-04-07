lado1 = float(input('Digite o valor do lado 1:\n'))
lado2 = float(input('Digite o valor do lado 2:\n'))
lado3 = float(input('Digite o valor do lado 3:\n'))

while lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2+lado3 > lado1:
    if lado1 == lado2 == lado3:
        triângulo = 'Triângulo Equilátero'
        print(triângulo)
        break
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        triângulo = 'Triângulo Isósceles'
        print(triângulo)
        break
    elif lado1 != lado2 != lado3:
        triângulo = 'Triângulo Escaleno'
        print(triângulo)
        break
input()
