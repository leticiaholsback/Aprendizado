listadeEstudantes = []
#................... COMEÇO cadastrarEstudante ...............
def cadastrarEstudante(ru):
    print('Bem vindo ao CADASTRAR de estudantes')
    print(' O RU do estudante a ser cadstrado é: {}'.format(ru))
    nome = input('Digite o nome do estudante')
    turma = input('Digite a turma do estudante')
    dicionarioEstudante = {'ru': ru,
                           'nome': nome,
                           'turma': turma}
    listadeEstudantes.append(dicionarioEstudante.copy())

    #................... FIM cadastrarEstudante ...............

# ................... COMEÇO consultarEstudante ...............
def consultarEstudante():
    while True:
        try:
            print('Bem vindo ao CONSULTAR de estudantes')
            opConsultar = int(input('Ente com a opcao desejada: \n'
                                    '1 consultar todos \n'
                                    '2 consultar ru \n'
                                    '3 consultar por turma \n'
                                    '4 retornar\n'))
            if opConsultar == 1:
                print('Bem vido a CONSULTAR TODOS')
                for estudante in listadeEstudantes: #selecionar cada dicionario da lista (cada estudante)
                    for key, valeu in estudante.items(): #selec cada conj chave\valor (ex larissa)
                        print('{} :{}' .format(key,value))
            elif opConsultar ==2:
                print('Bem vindo a opçao RU')
                entrada = int(input('digite o RU desejado: '))
                for estudante in listadeEstudantes:
                    if(estudante['ru'] == entrada):
                        for key, valeu in estudante.items():
                            print('{} :{}'.format(key, value))

            elif opConsultar ==3:
                print('Bem vindo a opçao TURMA')
                entrada = input('digite    TURMA desejado: ')
                for estudante in listadeEstudantes:
                    if (estudante['turma'] == entrada):
                        for key, valeu in estudante.items():
                            print('{} :{}'.format(key, value))
            elif opConsultar ==4:
                break
            else:
                print('NAO digite numeros que nao existem no menu')
        except ValueError:
            print('Não digite valores não inteiros')


# ................... FIM consultarEstudante ...............



# ................... COMEÇO removerEstudante ...............
def removerEstudante():
    print('Bem vindo ao REMOVER de estudantes')
    entrada = int(input('digite   RU desejado: '))
    for estudante in listadeEstudantes:
        if (estudante['ru'] == entrada):
            listadeEstudantes.remove(estudante)


# ................... FIM removerEstudante ...............


# ................... COMEÇO MAIN ...............
print('Bem vindo ao PROGRAMA DE CONTORLE DA LETICIA')
regtistroacademico = 0
while True:
    try:
        opcao = int(input( 'Digite a opcao desejada: \n 1 - Cadastrar estudantes \n 2 - consultar estudante \n 3 - remover estudante \n 4 - sair'))
        if opcao ==1:
            regtistroacademico = regtistroacademico +1
            cadastrarEstudante(regtistroacademico)
        elif opcao ==2:
            consultarEstudante()
        elif opcao == 3:
            removerEstudante()
        elif opcao ==4:
            print('programa finalizado')
            break
        else:
            print('nao digite numeros que nao existem no menu')
    except ValueError:
        print('Não digite valores não inteiros')



# ................... FIM MAIN...............

