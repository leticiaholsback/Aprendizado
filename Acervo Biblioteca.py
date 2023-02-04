import time
listadeLivro = []
#................... COMEÇO cadastrarAcervo ...............
def cadastrarLivro(cod):
    print(10*'|', 'Bem vindo ao CADASTRO de Livros', 10*'|')
    time.sleep(1)
    print(' O Codigo da LIVRO a ser cadstrado será: {}'.format(cod))
    nome = input('Digite o nome da Livro:\n>>>>')
    autor = input('Digite o Autor do Livro:\n>>>')
    dicionarioLivro = {'cod': cod,
                           'nome': nome,
                           'autor': autor}
    listadeLivro.append(dicionarioLivro.copy())

    #................... FIM cadastrarEstudante ...............
# ................... COMEÇO consultarEstudante ...............
def consultarLivro():
    while True:
        try:
            print(10*'|','Bem vindo ao CONSULTAR Acervo' ,10*'|')
            time.sleep(1)
            opConsultar = int(input('Escolha a opcao desejada:\n '
                                    '1 Consultar todo Acervo Disponivel para Emprestimo \n '
                                    '2 Consultar por Autor \n '
                                    '3 Retornar ao Menu \n >>>'))
            time.sleep(1)
            if opConsultar == 1:
                print(10*'|','Bem vido a CONSULTAR ACERVO DE LIVROS',10*'|')
                for cod in listadeLivro: #selecionar cada dicionario da lista (cada estudante)
                    for key, values in cod.items(): #selec cada conj chave\valor (ex larissa)
                        print('{} :{}' .format(key,values))

            elif opConsultar ==2:
                print('Bem vindo a opçao CONSULTA por AUTOR')
                entrada = input('Digite o AUTOR desejado: \n >>>')
                for cod in listadeLivro:
                    if (cod['autor'] == entrada):
                        for key, values in cod.items():
                            print('{} :{}'.format(key, values))
                            time.sleep(1)
            elif opConsultar ==3:
                break
            else:
                print('NAO digite Autores que nao existem no Acervo. Consulte corretamente nosso Acervo de livros')
        except ValueError:
            print('Não digite numeros')


# ................... FIM consultarLivro ...............

# ................... COMEÇO emprestarLivro ...............
def emprestar():
    print(10*'|','Bem vindo ao EMPRESTAR LIVRO!',10*'|')
    aluno = input('Digite seu nome para separar o livro: \n >>>')
    dias = input ('Digite quantos dias deseja ficar com o livro, nao passe de 10 dias: \n>>>')
    entrada = input('Digite o NOME do livro que consta na lista: ')
    for nome in listadeLivro:
        if (nome['nome'] == entrada):
            listadeLivro.remove(nome)
        print ('Olá {}, você já pode retirar o livro escolhido: {} . Por {} dias. \n Nao se esqueca de devolver dentro do prazo'.format (aluno,entrada, dias))
        time.sleep(2)

# ................... FIM removerEstudante ...............

# ................... COMEÇO MAIN ...............
print('..|..Bem vindo ao PROGRAMA DE ACERVO DE LIVROS DA ESCOLA MUNICIPAL DE ORIZONA..|..')
time.sleep(1)
print(5*' ','._.\n')
time.sleep(1)

registroLivro = 0
while True:
    try:
        opcao = int(input( 'Digite a opcao desejada: \n 1 - Cadastrar LIVRO \n 2 - Consultar Acervo de Livros \n 3 - Emprestar um Livro \n 4 - Sair \n >>>'))
        if opcao ==1:
            registroLivro = registroLivro +1
            cadastrarLivro(registroLivro)
        elif opcao ==2:
            consultarLivro()
        elif opcao == 3:
            emprestar()
        elif opcao ==4:
            print('Programa Finalizado. Obrigada!')
            break
        else:
            print('Nao digite numeros que nao existem no menu')
    except ValueError:
        print('Não digite valores não inteiros')


# ................... FIM MAIN...............
