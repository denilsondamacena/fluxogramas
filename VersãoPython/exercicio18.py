valor1=int(input("Digite o primeiro valor inteiro: "))
valor2=int(input("Digite o segundo valor inteiro: "))
if valor1 > valor2:
    dif=valor1-valor2
else:
    dif=valor2-valor1
print("A diferença do maior número para o menor é de {}".format(dif))