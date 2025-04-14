alunos = int(input("Digite o número de alunos: "))
soma = 0
x = 1
while x <= alunos:
    vl = float(input("Quais as notas dos alunos?"))
    soma+= vl
    x = x+1
media = soma/alunos
print(media)
