aluno = input('Digite o nome do aluno:\n')
nota1 = float(input('Digite a nota 1 do aluno:\n'))
nota2 = float(input('Digite a nota 2 do aluno:\n'))
média = (nota1 + nota2)/2

if média <= 10 and média >= 9:
    print('O aluno %s obteve conceito A! Sua nota final é %s' % (aluno, média))

elif média < 9 and média >= 7.5:
    print('O aluno %s obteve conceito B! Sua nota final é %s' % (aluno, média))

elif média < 7.5 and média >= 6:
    print('O aluno %s obteve conceito C! Sua nota final é %s' % (aluno, média))

elif média < 6 and média >= 4:
    print('O aluno %s obteve conceito D! Sua nota final é %s' % (aluno, média))

elif média < 4 and média >= 0:
    print('O aluno %s obteve conceito E! Sua nota final é %s' % (aluno, média))
input()
