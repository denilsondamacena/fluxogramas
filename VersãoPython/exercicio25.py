h1=int(input("Digite a hora (HH) do início do jogo: "))
m1=int(input("Digite os minutos (MM) do início do jogo: "))
h2=int(input("Digite a hora (HH) do final do jogo: "))
m2=int(input("Digite os minutos (MM) do final do jogo: "))
inicio=(h1*60+m1)
fim=(h2*60+m2)
if fim<inicio:
    fim=(fim+24*60)
duracao=fim-inicio
horas=(duracao//60)
minutos=(duracao%60)
print("O jogo durou {} horas e {} minutos".format(horas,minutos))