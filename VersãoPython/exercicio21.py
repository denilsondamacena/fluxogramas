n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
n4=float(input("Digite a quarta nota: "))
media=((n1+n2+n3+n4)/4)
if media >=6.0:
    print("Sua média é {:.1f} = Aprovado".format(media))
elif media >=3.0:
    print("Sua média é {:.1f} = Exame".format(media))
else:
    print("Sua média é {:.1f} = Retido".format(media))