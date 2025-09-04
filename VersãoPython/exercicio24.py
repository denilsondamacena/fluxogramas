valor=int(input("Digite um número: "))
if (valor%2==0) and (valor%3==0):
    print("O número é divísivel por 2 e 3")
elif (valor%2==0) and (valor%3!=0):
    print("O número é divísivel por 2 mas não é por 3")
elif (valor%2!=0) and (valor%3==0):
    print("O número não é divísivel por 2 mas é por 3")
else:
    print("O número não é divísivel por 2 e 3")