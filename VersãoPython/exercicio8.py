deposito=float(input("Digite o valor do depósito na poupança: "))
rendimento=(deposito*0.013)
valor_final=(deposito+rendimento)
print("O novo valor após um mês de aplicação é de: {}".format(valor_final))