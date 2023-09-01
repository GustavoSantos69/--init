#LOOPING#

nome = str(input('Digite seu nome: '))
materia =  str(input('Digite sua matéria: '))
l = 0
c = 0
matriz = [[0 for _ in range(c)] for _ in range(l)]
                   

nota1 = float(input('Digite a nota do 1° bimestre: '))
while ((nota1 < 0) or (nota1 > 10)):
    print('Nota do primeiro bimestre inválida! verifique')
    nota1 = float(input('Digite a nota do 2° bimestre: '))
    for l in matriz:
        matriz [0][1] = nome
        print(nome)

  
nota2 = float(input('Digite a nota do 2° bimestre: '))
while ((nota2 < 0) or (nota2 > 10)):
    print('Nota do segundo bimestre inválida! verifique')
    nota2 = float(input('Digite a nota do 2° bimestre: '))

nota3 = float(input('Digite a nota do 3° bimestre: '))
while ((nota3 < 0) or (nota3 > 10)):
    print('Nota do terceiro bimestre inválida! verifique')
    nota3 = float (input('Digite a nota do 3° bimestre: '))

nota4 = float(input('Digite a nota do 4° bimestre: '))
while ((nota4 < 0) or (nota4 > 10)):
    print('Nota do quarto bimestre inválida! verifique')
    nota4 = float(input('Digite a nota do 4° bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/4


if ((media > 10) or (media < 0)):
    print("Média INVÁLIDA !!! ERRO")
elif (media >= 7):
    print(nome,'',media,'APROVADO')
elif (media <= 5):
    print(nome,'', media,'RECUPERAÇÃO')
else:
    print(nome,'', media, 'REPROVADO!' )


matriz [0][2] = ma
matriz [0][3] = nota1
matriz [0][4] = nota2
matriz [0][5] = nota3
matriz [0][6] = nota4
matriz [0][7] = media

for l in matriz:
    print(l = 1)


