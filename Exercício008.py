produto1 = float(input('Digite o preço do produto 1:\n'))
produto2 = float(input('Digite o preço do produto 2:\n'))
produto3 = float(input('Digite o preço do produto 3:\n'))

if produto1 < produto2 and produto1 < produto3:
    print('O produto mais barato é o produto 1.')
elif produto2 < produto1 and produto2 < produto3:
    print('O produto mais barato é o produto 2.')
else:
    print('O produto mais barato é o produto 3.')
input()
