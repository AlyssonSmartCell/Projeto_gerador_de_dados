from random import randint
print("""
Bem-vindo ao gerador de dados para testes!
-----------------------------------------------------------
Com este gerador e possivel gerar os seguintes dados:
[1] Nome
[2] Email
[3] Telefone
[4] Cidade
-----------------------------------------------------------
OBS:Digite as opções separando-as po uma ',' ex: (1,2,3...)
""")

opçoes = input("Digite uma ou mais opções: ")

nomes = ["Alysson", "nathalia", "selma", "yasmin", "gustavo"]
emails = ["alysson@gmail.com", "selma@gmail.com", "gustavo@gmail.com", "nathalia@gmail.com", "yasmin@gmail.com"]
telefones = ["7865594-8776", "9806654-5467", "1238897-9876", "4398806-6484", "679 0054- 4678"]
cidade = ["Londrina", "Maringa", "cascavel", "Sao Paulo", "Jundiai"]



tela_inicial = True
while tela_inicial == True:
    if opçoes == "1":
        aleatorio = randint(0, 4)
        print(nomes[aleatorio])
        break
    
    elif opçoes == "2":
        aleatorio = randint(0, 4)
        print(emails[aleatorio])
        break

    


deseja_continuar = input("Deseja continuar (s/n): ")

