valor1=int(input("Digite o primeiro número: "))
valor2=int(input("Digite o segundo número: "))
while valor2<valor1:
    print("Digite um número maior")
    valor2=int(input("Digite novamente o segundo número: "))
valor3=int(input("Digite o terceiro número: "))
while valor3<valor2:
    print("Digite um número maior")
    valor3=int(input("Digite novamente o terceiro número: "))
valor4=int(input("Digite o quarto número: "))
if valor4<=valor1:
    print("Ordem crescente {},{},{},{}".format(valor4,valor1,valor2,valor3))
elif valor4<=valor2:
    print("Ordem crescente {},{},{},{}".format(valor1,valor4,valor2,valor3))
elif valor4<=valor3:
    print("Ordem crescente {},{},{},{}".format(valor1,valor2,valor4,valor3))
else:
    print("Ordem crescente {},{},{},{}".format(valor1,valor2,valor3,valor4))
