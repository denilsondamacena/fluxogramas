poupanca=0.03
rendafixa=0.05

investimento=int(input("Escolha o tipo de investimento: \n (1) poupança \n (2) renda fixa \nDigite a opção:"))
if investimento==1:
    valororiginal=float(input("Digite o valor investido: "))
    juros=(valororiginal*poupanca)
    corrigido=(valororiginal+juros)
    print("O valor corrigido após 30 dias é de R${}".format(corrigido))
elif investimento==2:
    valororiginal=float(input("Digite o valor investido: "))
    juros=(valororiginal*rendafixa)
    corrigido=(valororiginal+juros)
    print("O valor corrigido após 30 dias é de R${}".format(corrigido))
else:
    print("Demais tipos não serão considerados.")