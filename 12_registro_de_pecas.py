listadePecas = []
#................... COMEÇO cadastrarPeca ...............
def cadastrarPeca(cod):
    print('Bem vindo ao CADASTRAR PEÇAS')
    print(' O Codigo da PEÇA a ser cadstrada é: {}'.format(cod))
    nome = input('Digite o nome da Peça')
    fabricante = input('Digite a fabricante da Peça:')
    valor = input ('Digite o Valor da Peça:')
    dicionarioPeca = {'Código da Peça': cod,
                           'nome': nome,
                           'fabricante': fabricante,
                           'valor': valor}
    listadePecas.append(dicionarioPeca.copy())

    #................... FIM cadastrarEstudante ...............

# ................... COMEÇO consultarEstudante ...............
def consultarPeca():
    while True:
        try:
            print('Bem vindo ao CONSULTAR Peça')
            opConsultar = int(input('Ente com a opcao desejada: \n'
                                    '1 Consultar todos \n'
                                    '2 Consultar Codigo \n'
                                    '3 Consultar por Fabricante \n'
                                    '4 retornar\n'))
            if opConsultar == 1:
                print('Bem vido a CONSULTAR TODAS AS PEÇAS')
                for peca in listadePecas: #selecionar cada dicionario da lista (cada estudante)
                    for key, valeus in peca.items(): #selec cada conj chave\valor (ex larissa)
                        print('{} :{}' .format(key,values))
            elif opConsultar ==2:
                print('Bem vindo a opçao CÓDIGO')
                entrada = int(input('digite o CÓDIGO desejado: '))
                for peca in listadePecas:
                    if(peca ['codigo'] == entrada):
                        for key, valeus in peca.items():
                            print('{} :{}'.format(key, values))

            elif opConsultar ==3:
                print('Bem vindo a opçao FABRICANTE')
                entrada = input('digite o FABRICANTE desejado: ')
                for peca in listadePecas:
                    if (peca['fabricante'] == entrada):
                        for key, valeus in peca.items():
                            print('{} :{}'.format(key, values))
            elif opConsultar ==4:
                break
            else:
                print('NAO digite números que nao existem no menu')
        except ValueError:
            print('Não digite valores não inteiros')


# ................... FIM consultarPeca ...............



# ................... COMEÇO removerPeca ...............
def removerPeca():
    print('Bem vindo ao REMOVER peças')
    entrada = int(input('digite  código desejado: '))
    for peca in listadePecas:
        if (peca['código'] == entrada):
            listadePecas.remove(peca)


# ................... FIM removerEstudante ...............


# ................... COMEÇO MAIN ...............
print('Bem vindo ao PROGRAMA DE CONTORLE DA LETICIA')
registroPeca = 0
while True:
    try:
        opcao = int(input( 'Digite a opcao desejada: \n 1 - Cadastrar peça \n 2 - Consultar Peça \n 3 - Remover Peça \n 4 - Sair'))
        if opcao ==1:
            registropeca = registroPeca +1
            cadastrarPeca(registroPeca)
        elif opcao ==2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao ==4:
            print('Programa Finalizado')
            break
        else:
            print('nao digite numeros que nao existem no menu')
    except ValueError:
        print('Não digite valores não inteiros')



# ................... FIM MAIN...............
