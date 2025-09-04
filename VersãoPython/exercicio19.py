valor1=float(input("Digite o primeiro valor real: "))
valor2=float(input("Digite o segundo valor real: "))
if valor1>valor2:
    print("O maior valor é {}".format(valor1))
else:
    if valor2==valor1:
        print("Os dois são iguais.")
    else:
        print("O maior valor é {}".format(valor2))