poupanca = 0.03
rendafixa = 0.05         
investimento = int(input("Escolha o tipo de investimento: \n (1) poupança \n (2) renda fixa \nDigite a opção: "))

if investimento == 1:
    valororiginal = float(input("Digite o valor investido: "))
    dias = int(input("Digite o número de dias: "))
    taxa_mensal=poupanca
    taxa_diaria = (1 + taxa_mensal)**(1/30) - 1
    corrigido = valororiginal * (1 + taxa_diaria)**dias
    print("O valor corrigido após 30 dias é de R${:.2f}".format(corrigido))
elif investimento == 2:
    valororiginal = float(input("Digite o valor investido: "))
    dias = int(input("Digite o número de dias: "))
    taxa_mensal=rendafixa
    taxa_diaria = (1 + taxa_mensal)**(1/30) - 1 
    corrigido = valororiginal * (1 + taxa_diaria)**dias
    print("O valor corrigido após {} dias é de R${:.2f}".format(dias,corrigido))
else:
    print("Demais tipos não serão considerados.")