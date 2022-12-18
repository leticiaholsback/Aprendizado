import os

os.getcwd() #consigo ver o caminho do diretorio
os.listdir('c:\\Users\\dvalv\\Downloads') # consigo ver os documentos do meu diretorio

################ inicio do código
diretorio = os.getcwd() #criei uma variavel para trabalhar no diretorio cwd

full_list = os.listdir(diretorio) # criando uma lista com o diretorio
files_list=[i for i in full_list if os.path.isfile (i) and'.py' not in i]
#para todo arquivo na lista, so quero arquivos e não quero arquivos pyton

types = list(set([i.split('.')[-1] for i in files_list]))
#set = não deixar repetir os elementos do mesmo tipo de arquivo de origem (xls, mp4....)
# ([i.split('.')[-1]  todo o nome de arquivo com ponto, vai separar e pegar o ultimo elemento (-1)

for file_type in types:
    os.mkdir(file_type)
#para td tipo de arquivo criar uma pasta com o nome do tipo do arquivo CRIANDO PASTAS

for file in files_list:
    from_path= os.path.join(diretorio,file) # onde o arq está e ja agrupa os arquivos (DE)
    to_path= os.path.join(diretorio,file.split('.')[-1], file) # para onde vão os arq agrupados (PARA)
#NESSE FOR as duas primeiras linhas, separa os arquivos por tipo na pasta Download
#na terceira linha pega os arquivos separados e insere na sua pasta nonimada com o tipo de arquivo

#só vai ficar executado a partir desse proximo comando    
    os.replace(from_path, to_path)
#executa, replace substitui os arq de from_path para to_path, dessa forma todos os arquivos estão
#agrupados nas devidas pastas
