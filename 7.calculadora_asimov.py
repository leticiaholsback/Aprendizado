import os
import time

def calculadora():
    print('||||||||||||||| BEM VINDO A CALCULADORA |||||||||||||||||')
    menu= print('Escolha o que deseja: \n 1. ADIÇÃO \n 2. SUBTRAÇÃO \n 3. MULTIPLICAÇÃO \n 4. DIVISÃO \n 5. EXPONENCIAÇÃO \n')
    escolha=int(input('Escolha:'))

    while True:
        if escolha == 1:
            print('Sua escolha foi ADIÇÃO\n Digite o primeiro número')
            n1 = float(input())
            print('Digite o Segundo número')
            n2 = float(input())
            soma= n1+n2
            print('O valor da soma é {}'.format(soma))

        elif escolha == 2:
            print('Você escolheu SUBTRAÇÃO\n Digite o primeiro número')
            n1 = float(input())
            print('Digite o Segundo número')
            n2 = float(input())
            sub= n1-n2
            print('O valor da subtração é {}'.format(sub))

        elif escolha == 3:
            print('Você escolheu MULTIPLICAÇÃO\n Digite o primeiro número')
            n1 = float(input())
            print('Digite o Segundo número')
            n2 = float(input())
            multi= n1*n2
            print('O valor da subtração é {}'.format(multi))

        elif escolha == 4:
            print('Você escolheu DIVISÃO\n Digite o primeiro número')
            n1 = float(input())
            print('Digite o Segundo número')
            n2 = float(input())
            div= n1/n2
            print('O valor da subtração é {}'.format(div))

        elif escolha == 5:
            print('Você escolheu EXPONENCIAÇÃO\n Digite o primeiro número')
            n1 = float(input())
            print('Digite o Segundo número')
            n2 = float(input())
            exp = n1 ** n2
            print('O valor da  é {}'.format(exp))
            time.sleep(1)
        print('||| Deseja realizar mais alguma Operação?||| \n (S) SIM\n (N) NÃO \n')
        if input() == 's':
            calculadora()
        elif input() == 'n':
            print('Operação Finalizada!')
            break

calculadora()
