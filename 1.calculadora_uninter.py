class calculadora:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0

    def somar(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 + self.num2
        return self.resultado

    def subtrair(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 - self.num2
        return self.resultado

    def multiplicar(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 * self.num2
        return self.resultado

    def dividir(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 / self.num2
        return self.resultado

    def expoente(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 ** self.num2
        return self.resultado

    def resto(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 % self.num2
        return self.resultado

def continuar(entrada):
    if entrada:
        return True
    else:
        return False

def menu():
    opc = {1:'Adição',
           2: 'Subtração',
           3: 'Multiplicação',
           4: 'Divisão',
           5: 'Exponenciação'
           6: 'Módulo (resto)'}

    calc = calculadora ()        #varivevel para chamar a class
    print("""Você quer realizar qual operação matemática?
    1 -> Adição
    2 -> Subtração
    3 -> Multiplicação
    4 -> Divisão
    5 -> Exponenciação
    6 -> Módulo (resto)
    Digite o número desejado e aperte ENTER""")
    calcular = True
    while calcular:
        opcao = input('\n Escolha a opção desejada (,1,2,3,4,5 ou 6)')
        if not(opcao in '1 2 3 4 5 6'):
            print('Opção escolhida é invalida!')
            continue
        else:
            opcao = int(opcao)
            print(f"A operacão escolhida é {op[opcao]}")





