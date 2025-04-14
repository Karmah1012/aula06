tentativa = 1
senha = "5555"
x = input("Digite sua senha: ")
c = "Senha bloqueada"
while x != senha:
    x = input("Digite outra vez: ")
    tentativa = tentativa + 1
    if tentativa == 3 :
     print(c)
if senha == x:
    print("Senha correta, o professor está feliz! ")


