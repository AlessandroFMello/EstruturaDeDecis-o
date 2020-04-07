from decimal import Decimal
salário = float(input('Digite o salário: \n'))

if salário <= 280:
    print('O salário era: R$', salário)
    print('O aumento foi de 20%')
    salárionovo = salário * 1.2
    Aumento = salárionovo - salário
    print('O aumento foi de: R$ %f' % Aumento)
    print('O novo salário é: R$ %f' % salárionovo)
elif salário > 280 and salário <= 700:
    print('O salário era: R$', salário)
    print('O aumento foi de 15%')
    salárionovo = salário * 1.15
    Aumento = salárionovo - salário
    print('O aumento foi de: R$ %f' % Aumento)
    print('O novo salário é: R$ %f' % salárionovo)
elif salário > 700 and salário <= 1500:
    print('O salário era: R$', salário)
    print('O aumento foi de 10%')
    salárionovo = salário * 1.10
    Aumento = salárionovo - salário
    print('O aumento foi de: R$ %f' % Aumento)
    print('O novo salário é: R$ %f' % salárionovo)
elif salário > 1500:
    print('O salário era: R$', salário)
    print('O aumento foi de 5%')
    salárionovo = salário * 1.05
    Aumento = salárionovo - salário
    print('O aumento foi de: R$ %f' % Aumento)
    print('O novo salário é: R$ %f' % salárionovo)
input()
