import os
clear = lambda: os.system('cls')

carros = [
    ('GM Celta 1.0', 75),
    ('GM Classic 1.0', 85),
    ('Fiat Novo Uno 1.0', 90),
    ('Renault Sandero 1.0', 95),
    ('Ford Focus Hatch 1.6', 110),
    ('Duster 2.0 Automatica', 130),
    ('Ford Ranger 2.2', 260),
    ('Porsche 911', 475),
    ('Mitsubishi Pajeto TR4', 180)
]

alugados = []

def lista_de_carros(lista_carros):
    for i, car in enumerate (lista_carros):
        print ('[{}] {} - R$ {} por dia.'.format(i, car[0], car[1]))

while True:
    clear()
    print('|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|\n Bem Vindo a Locadora de Carros! \n |.|.|.|.|.|.|.|.|.|.|.|.|.|.|.| \n')
    print('Digite a Opção com o que você deseja?')
    print(' (0) OLHAR O PORTIFÓLIO \n (1) ALUGAR UM CARRO \n (2) DEVOLVER UM CARRO \n ATENÇÂO! Digite apenas essas opções para que sistema não seja encerrado!')
    op = int(input())

    clear()
    if op ==0:
        lista_de_carros(carros)
    elif op == 1:
        lista_de_carros(carros)
        print('Você escolheu Alugar um carro! \n Escolha o código do carro que você quer alugar:')
        cod_car = int(input())
        print('Você quer alugar por quantos dias?')
        dias = int(input())
        clear()
        print('Você escolheu o Veiculo {} por {} dias.'.format(carros[cod_car] [0], dias))
        print('O aluguel vai custar {}. Deseja alugar?'.format(dias*carros[cod_car][1]))
        print(' Digite (0) para SIM\n Digite (1) para NÃO')
        confere = int(input())
        if confere == 0:
            print('Você alugou o veículo {} por {}, Pode retirar o seu carro!'.format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
            print("Não exite carro para devolver.")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            lista_de_carros(alugados)
            print("\n Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if confere == 0:
                print('Obrigada por devolver o carro {}\n'.format(alugados[cod][0]))
                carros.append(alugados.pop(cod))
    print('|.|.|.|.|.|.|.|.|.|')
    print('0 para CONTINUAR | 1 para SAIR')
    if float(input()) == 1:
        print('Obrigada! Sistema Finalizado')
        break




