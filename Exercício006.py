num1 = float(input('Digite um número:\n'))
num2 = float(input('Digite outro número:\n'))
num3 = float(input('Digite outro número:\n'))

if num1 > num2 and num1 > num3:
    print('O maior número é', num1)
elif num2 > num1 and num2 > num3:
    print('O maior número é:', num2)
else:
    print('O maior número é', num3)
input()
