import random
import time
from random import randint
import os
from os import system

contagem_jogador=0
contagem_computador=0
placar= [0,0]
jogadas=0
#variavel ppt para inserir Pedra, papel e tesoura
ppt =('Pedra', 'Papel', 'Tesoura')
jogada_computador = randint(0,2) #sorteio do computador de valores de 1 a 3
print (10*'||', 'BEM VINDO AO JOGO PEDRA, PAPEL E TESOURA', 10*'||')
time.sleep (2)

def inicio(placar):
    while jogadas !=1:
        print('Escolha a sua Opcao: \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA')
        jogador= int(input( 'Digite o numero que voce quer\n'))
        print (10* '||')
        print (6*' ','VAMOS')
        time.sleep (1)
        print (7*' ','LA')
        print (10*'||')
        time.sleep (1)
        print (f'Você jogou: {ppt[jogador]}')
        print(f'Seu oponente jogou: {ppt[jogada_computador]}')
        print (5*'|.|.')
        time.sleep(1)

        if jogada_computador == 0: #SE O COMPUTADOR JOGAR 0 = PEDRA
            if jogador ==0:
                print ('EMPATE')
                placar[0] += 0
            elif jogador ==1:
                print ('VOCE GANHOU!')
                placar[0] += 1
            elif jogador ==2:
                print ('VOCE VACILOU, PERDEU')
                placar[1] += 1
            else:
                print ('Escolha as opcoes corretas!')

        if jogada_computador == 1: #SE O COMPUTADOR JOGAR 1 = Papel
            if jogador ==0:
                print ('VOCE VACILOU, PERDEU')
                placar[1] += 1
            elif jogador ==1:
                print ('EMPATE')
                placar[0] += 0
            elif jogador ==2:
                print ('VOCE GANHOU')
                placar[0] += 1
            else:
                print ('Escolha as opcoes corretas!')

        if jogada_computador == 2: #SE O COMPUTADOR JOGAR 2 = TESOURA
            if jogador ==0:
                print('VOCE GANHOU')
                placar[0] += 1
            elif jogador ==1:
                print ('VOCE VACILOU, PERDEU')
                placar[1] += 1
            elif jogador ==2:
                print('EMPATE')
                placar[0] += 0
            else:
                print('Escolha as opcoes corretas!')

        while True:
            time.sleep(1)
            print(5 * '.', 'PLACAR', '.' * 5)
            print('Voce: {}'.format(placar[0]))
            print('Oponente: {}'.format(placar[1]))
            time.sleep(2)
            print('Deseja jogar novamente? Digite letra MAIUSCULA: (S) SIM (Q) Sair')
            if input()=='S':
                inicio(placar)
            elif input()!='S':
                print('Operacao Finalizada')
            break

os.system('cls')
inicio(placar)

