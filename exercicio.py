# Faça um programa em Python que leia as notas de prova de N alunos (N deve ser lido, validado - no máximo 50) e armazene em uma lista. Calcule e escreva:
#     ◦ A maior nota da turma;
#     ◦ A menor nota da turma;
#     ◦ A média da turma na prova;
#     ◦ A porcentagem de notas maior ou igual a 7;
#     ◦ A porcentagem de notas menor do que 7.

notas =[]
quantidade = int(input('Quantos notas serao inseridas?(max 50):'))

def VerificarNota(nota):
    while True:
        if nota > 100 or nota < 0:
            nota = float(input("Valor incorreto, digite uma nota de 0 a 100:"))
        else:
            return nota

def notasMaioresEMenores(notas, maior):
    result = None
    if(maior):
        result = list(filter(lambda x: x >= 7.0, notas))
    else:
        result = list(filter(lambda x: x < 7.0, notas))

    return float(len(result))/float(len(notas)) * 100

if(quantidade <=50):
    for i in range(quantidade):
        notas.append(VerificarNota(float(input('digite a '+str(i+1)+' nota:'))))

    print("maior nota:"+str(max(notas, key=int)))
    print("menor nota:"+str(min(notas, key=int)))
    print("media das notas:"+str(sum(notas)/len(notas)))
    print("Maiores que sete: "+str(notasMaioresEMenores(notas, True))+" %")
    print("Maiores que sete: "+str(notasMaioresEMenores(notas, False))+" %")

else:
    print('Valor Incorreto! Tente novamente')

