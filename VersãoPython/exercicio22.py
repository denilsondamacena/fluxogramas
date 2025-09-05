valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segundo valor diferente do primeiro: "))
while valor1==valor2:
    print("Os valores são iguais.")
    valor2=int(input("Digite o segundo valor novamente: "))
if valor1<valor2:
    print("Os valores em ordem crescente são {},{}".format(valor1,valor2))
else:
    print("Os valores em ordem crescente são {},{}".format(valor2,valor1))