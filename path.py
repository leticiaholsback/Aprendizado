import os


os.getcwd()

os.path.join(os.getcwd(), 'CrieiPasta')  # mescla strings

os.path.basename(os.getcwd()) #retorna o nome só da ultima pasta

os.getcwd().split('\\') [-1]

os.path.split(os.getcwd()) # saiu o \\ so ultimo item

os.path.dirname(os.getcwd()) #antepenultimo

cur_dir= os.getcwd()
os.path.getmtime(cur_dir) #executa o tempo em seg de uma forma ambigua, nao gera conincidencia

cur_dir= os.getcwd()
lt = os.path.getmtime(cur_dir) 
from datetime import datetime #importando a biblioteca
datetime.utcfromtimestamp(lt) # mostra dia, mes ano, segundos e milisegundos
#por ser em segundo é boa para operações de matematica

os.path.isfile(cur_dir) #se o diretorio é uma arquivo, senao é False