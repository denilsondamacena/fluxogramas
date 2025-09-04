A=int(input("Digite o valor do coeficiente A: "))
B=int(input("Digite o valor do coeficiente B: "))
C=int(input("Digite o valor do coeficiente C: "))
delta=((B**2)-4*A*C)
if delta > 0:
    x1=(-B+(delta**0.5))/(2*A)
    x2=(-B-(delta**0.5))/(2*A)
    print("As raízes reais de delta são: {},{}".format(x1,x2))
else:
    print("Não existe raízes reais.")