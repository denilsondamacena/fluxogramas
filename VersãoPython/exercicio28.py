precoatual=float(input("Digite o preço atual do produto: "))
media=float(input("Digite a média mensal de vendas do produto: "))
if media<500 and precoatual<30:
    preconovo=(precoatual*1.10)
    print(f"O novo preço do produto é de R${preconovo:.2f} após ajuste de +10%")
elif 500<= media <1000 and 30<= precoatual<80:
    preconovo=(precoatual*1.15)
    print(f"O novo preço do produto é de R${preconovo:.2f} após ajuste de +15%")
elif media>=1000 and precoatual>=80:
    preconovo=(precoatual*0.95)
    print(f"O novo preço do produto é de R${preconovo:.2f} após ajuste de -5%")
else:
    preconovo=precoatual
    print("O preço não deve ser alterado")