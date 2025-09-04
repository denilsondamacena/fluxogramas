num1=int(input("Digite o primeiro número inteiro: "))
num2=int(input("Digite o segundo número inteiro: "))
if num1>num2:
    maior=num1
    menor=num2
else:
    maior=num2
    menor=num1
if menor!=0:
    if maior%menor==0:
        print("O maior número é múltiplo do menor.")
    else: 
        print("O maior número não é múltiplo do menor.")
else:
    print("Não é possível verificar múltiplo quando o menor é zero.")