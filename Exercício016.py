a = float(input('Digite o valor de a:\n'))
if a == 0:
    print('Se "a = 0" a equação não é do segundo grau')
else:
    b = float(input('Digite o valor de b:\n'))
    c = float(input('Digite o valor de c:\n'))
    delta = ((b**2) - (4*a*c))
    if delta < 0:
        print('A equação não possui raízes reais!')
    elif delta == 0:
        x = (-b)/(2*a)
        print('Delta igual a zero, então a equação possui uma raíz real que vale %s' % x)
    else:
        raiz = delta**0.5
        x1 = (-b + raiz) / 2 * a
        x2 = (-b - raiz) / 2 * a
        print('Delta maior que zero, então a equação possui duas raízes reais.\nX1 vale %s e X2 vale %s' % (x1, x2))
input()
