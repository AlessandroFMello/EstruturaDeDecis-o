valHora = float(input('Quanto você recebe por hora?\n'))
quantHora = float(input('Quantas horas você trabalha por mês?\n'))

salBruto = (valHora * quantHora)

if salBruto <= 900:
    IR = salBruto * 0
    inss = salBruto * 0.1
    fgts = salBruto * 0.11
    totalDesc = inss + IR
    salLiq = salBruto - totalDesc
    print('O salário bruto é:\nR$%s' % salBruto)
    print('o valor do imposto de renda é:\nR$%s' % IR)
    print('O valor a ser pago ao INSS é:\nR$%s' % inss)
    print('O valor a ser pago ao FTGS é:\nR$%s' % fgts)
    print('O total a ser descontado do salário é:\nR$%s' % totalDesc)
    print('O salário líquido é:\nR$%s' % salLiq)

elif salBruto <= 1500:
    IR = salBruto * 0.05
    inss = salBruto * 0.1
    fgts = salBruto * 0.11
    totalDesc = inss + IR
    salLiq = salBruto - totalDesc
    print('O salário bruto é:\nR$%s' % salBruto)
    print('o valor do imposto de renda é:\nR$%s' % IR)
    print('O valor a ser pago ao INSS é:\nR$%s' % inss)
    print('O valor a ser pago ao FTGS é:\nR$%s' % fgts)
    print('O total a ser descontado do salário é:\nR$%s' % totalDesc)
    print('O salário líquido é:\nR$%s' % salLiq)

elif salBruto <= 2500:
    IR = salBruto * 0.1
    inss = salBruto * 0.1
    fgts = salBruto * 0.11
    totalDesc = inss + IR
    salLiq = salBruto - totalDesc
    print('O salário bruto é:\nR$%s' % salBruto)
    print('o valor do imposto de renda é:\nR$%s' % IR)
    print('O valor a ser pago ao INSS é:\nR$%s' % inss)
    print('O valor a ser pago ao FTGS é:\nR$%s' % fgts)
    print('O total a ser descontado do salário é:\nR$%s' % totalDesc)
    print('O salário líquido é:\nR$%s' % salLiq)

elif salBruto > 2500:
    IR = salBruto * 0.2
    inss = salBruto * 0.1
    fgts = salBruto * 0.11
    totalDesc = inss + IR
    salLiq = salBruto - totalDesc
    print('O salário bruto é:\nR$%s' % salBruto)
    print('o valor do imposto de renda é:\nR$%s' % IR)
    print('O valor a ser pago ao INSS é:\nR$%s' % inss)
    print('O valor a ser pago ao FTGS é:\nR$%s' % fgts)
    print('O total a ser descontado do salário é:\nR$%s' % totalDesc)
    print('O salário líquido é:\nR$%s' % salLiq)
input()
