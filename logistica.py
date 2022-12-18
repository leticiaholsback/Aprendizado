#................. COMEÇO DA FUNÇÃO TAMANHO ...............

def dimensoesObjeto():
    while True:
        try:
            comprimento = int(input('Digite o COMPRIMENTO do objeto em cm: \n'))
            return comprimento
        except ValueError:
            print('Você digitou algo errado! Digite apenas números. Tente novamente.')
            continue

def perguntaLA():
    while True:
        try:
            largura = int(input('Digite a LARGURA do objeto em cm: \n'))
            return largura
        except ValueError:
            print('Você digitou algo errado! Digite apenas números. Tente novamente.')


def perguntaAL():
    while True:
        try:
            altura = int(input('Digite a ALTURA do objeto em cm: \n'))
            return altura
        except ValueError:
            print('Você digitou algo errado! Digite apenas números. Tente novamente.')
            continue


def calcularDimensao(comprimento,altura,largura):
    dimensao = comprimento * altura * largura
    while True:
        try:
            if dimensao <= 100000:
                return dimensao
            else:
                print('A dimensão informada não é aceita pela CIA')
            return dimensoesObjeto(),perguntaLA(), perguntaAL()
        except ValueError:
            print('Você digitou algo errado! Digite apenas números. Tente novamente.')
            continue


def calcularValorDimensao(dimensao):
    while True:
        try:
            if dimensao < 1000:
                return 10.00
            elif dimensao <= 1000 < 10000:
                return 20.00
            elif dimensao <= 10000 < 30000:
                return 30.00
            elif dimensao <= 30000 < 100000:
                return 50.00
            else:
                print('Essa dimensão não é aceita pela nossa companhia')
                return
        except ValueError:
            print('Você digitou algo errado! Digite apenas números. Tente novamente.')
            continue
#................. COMEÇO DA FUNÇÃO PESO .............

def pesoObjeto ():
    while True:
        try:
            pesoObjeto = float(input('Digite o PESO do objeto em KG (atenção, digite com ponto): \n '))
            if pesoObjeto < 0.1:
                return 1
            elif 0.1 <= pesoObjeto < 1:
                return 1.5
            elif 1 <= pesoObjeto < 10:
                return 2
            elif 10 <= pesoObjeto < 30:
                return 3
            else:
                print('Não aceitamos objetos tão pesados')
                continue
        except ValueError:
            print('Por favor, digite apenas números. Tente novamente.')
            continue

#................. COMEÇO DA FUNÇÃO ROTA ...............

def rotaObjeto():
    while True:
        try:
            rotaObjeto = input('Seleione a ROTA:\n RS - De Rio de Janeiro até São Paulo \n BS - De Brasília até São Paulo \n BR - De Brasília até Rio de Janeiro\n>>')
            if rotaObjeto == 'RS':
                return 1.0
            elif rotaObjeto == 'BS':
                return 1.2
            elif rotaObjeto == 'BR':
                return 1.5
            else:
                print('Você digitou uma rota que não existe')
                continue
        except ValueError:
            print('Atenção! Digite a Sigla correta da Rota')
            continue


#.................. COMEÇO DA MAIN .................
print('Bem vindo a Companhia Logística Letícia dos Santos Rolon SA!\n VAMOS COMEÇAR?')
comprimento = dimensoesObjeto()
largura = perguntaLA()
altura = perguntaAL()
dimensao = calcularDimensao(comprimento,largura,altura)
peso = pesoObjeto()
destino = rotaObjeto()
valorDimensao = calcularValorDimensao(dimensao)
print ('\n')
print('A caixa deverá ser conforme volume do objeto que em cm³ é: {:.2f}'.format(dimensao))
print('O valor para esta dimensão é R$: {}' .format(valorDimensao))
print('Peso é R$: {}'.format(peso))
print('Destino é : {}'.format(destino))
print('Total a Pagar é R$ {:.2f}' .format(valorDimensao * peso * destino))