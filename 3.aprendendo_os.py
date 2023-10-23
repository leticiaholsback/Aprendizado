import os

os.getcwd() #retorna uma string que da o caminho completo até onde estou

os.listdir('\\Users\\dvalv\\OneDrive\\Documentos\\') # nesse caso, mostrou todos os arquivos que estão na minha pasta Documento

#os.chdir #ele troca do diretorio que esta sendo executado
actual_dir= os.getcwd() #mostra o diretorio atual
os.chdir('\\Users\\dvalv\\OneDrive\\')
print(actual_dir) #mostra o diretorio primario do arquivo, pq fiz uma variaves na linha 8
os.chdir(actual_dir)
print(os.getcwd())

os.mkdir('CriaPasta') #criando pastas
os.mkdir('NovaPasta')
os.rename('teste.csv', 'teste2.csv')
os.rename('Segunda_pasta', 'Primeira_pasta')
#os.rename('CrieiPasta', 'Primeira_pasta/CrieiPasta') #colocoua CrieiPasta dentro da PrimeiraPasta
os.rename('Primeira_pasta/CrieiPasta', 'CrieiPasta') #volta ao que era antes

os.remove ('teste.csv') #exclui arquivos
os.rmdir('CriaPasta') #exclui pastas

cmd='date'
os.system(cmd)


#testando comit
