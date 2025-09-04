alimentoKG=float(input("Digite a quantidade de alimentos em quilogramas: "))
alimentoG=(alimentoKG*1000)
dias=(alimentoG/50)
print("O alimento durará {} dias se for consumido 50g por dia.".format(dias))