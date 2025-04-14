pa = float(input("Digite a primeira nota: "))
while pa < 0  or pa > 10 :
    pa = float(input("Valor fora da faixa, \n"
                     "Digite a nota1 novamente:"))
pu = float(input("Digite uma nota2 : "))
while pu > 10 or pu < 0 :
    pu = float(input("Valor2 fora da faixa:\n"
                     "Digite o valor 2 novamente: "))
media = (pa + pu) / 2
print(media)

