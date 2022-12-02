from random import randint 

entrada = list(input("digite os valores: "))

def entrada_de_dados(elemento):
    posicao_numero = 0

    for procura in range(len(entrada)):
        if elemento in entrada[procura]:
            posicao_numero = procura
            break
    return(posicao_numero)

final = entrada_de_dados("2")

print(final)
print(entrada)

