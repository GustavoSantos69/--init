

n = int(input('Digite a dimensão n da matriz: '))
m = int(input('Digite a dimensão m da matriz: '))
matriz = []
for i in range(n):
    matriz.append([]*m)
print(matriz)
f = 0
c = 0
i = 1



while i==1:
    nome = str(input("Digite o nome do aluno (a):"))
    matriz[f].append(nome)
    c+=1


    materia = str(input("Digite a matéria:"))
    matriz[f].append(materia)

    nota1 = float(input("Digite a nota do 1º Bimestre:"))
    while ((nota1<0) or(nota1>10)):
        print("Nota do 1º Bimestre:")
    matriz[f].append(nota1)

    nota2 = float(input("Digite a nota do 2º Bimestre: "))
    while ((nota2<0)or(nota2>10)):
            print("Nota do 2º Bimestre Invalida! Verifique ")
            nota2 = float(input("Digite a nota do 2º Bimestre:"))
    matriz[f].append(nota2)

    nota3 = float(input("Digite a nota do 3º Bimestre:"))
    while((nota3 < 0)or(nota3 > 10)):
        print("Nota do 4º Bimestre Invalida! Verifique:")
        nota3= float(input("Digite a nota do 3º Bimestre:"))
    matriz[f].append(nota3)

    nota4 = float(input("Digite a nota do 4º Bimestre:"))
    while ((nota4 < 0)or (nota4 >10)):
        print("Nota do 4º Bimestre Invalida! Verifique")
        nota4 = float(input("Digite a nota do 4º Bimestre:"))
    matriz[f].append(nota4)

    media = (nota1 + nota2 + nota3 + nota4)/4
    matriz[f].append(media)

    if((media >10)or (media <0)):
        print("Média Invalida !!! Erro")
    elif (media >=7):
        print(nome,"",media,"Aprovado!")
    elif(media >= 4):
        print(nome,"", media, "Recuperação!")
    else:
        print(nome,"",media, "Reprovado!")

    i=int(input("\nQuer cadastrar funcionarios? Digite '1' para 'Sim' ou '0' para sair.\nR:"))
    
		
        

    for i in range(10):
        for k in range(8):
            print(matriz[i][k])
    
            
          




