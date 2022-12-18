import pandas as pd

file_store = '../../OneDrive/Documentos/Stores.csv'
data_frame = pd.read_csv(file_store, sep=',')
data_frame = data_frame.rename(columns={'Store_Sales': 'VENDAS','Items_Available':'ITENS_DISPONÍVEIS','Store_Area':'ITENS',
                                        'Daily_Customer_Count':'VISITANTE','Store ID': 'ID'}) #ALTERANDO NOMES DAS COLUNAS
print('\nITENS_DISPONÍVEIS:')
dados= data_frame['ITENS_DISPONÍVEIS']
print(f'O valor máximo de ITENS_DISONÍVEIS é: {dados.values.max()}') #mostra o valor máximo
print(f'O valor mínimo de ITENS_DISONÍVEIS é: {dados.values.min()}') #mostra o valor minimo
print(f'O valor médio de ITENS_DISONÍVEIS é: {dados.values.mean()}') #mostra a média
print(f'O Desvio pdarão de ITENS_DISONÍVEIS é: {dados.values.std()}')  #mostra o desvio padrão

print('\nITENS:')
dados=data_frame['ITENS']
print(f'O valor máximo de ITENS é: {dados.values.max()}') #mostra o valor máximo
print(f'O valor mínimo de ITENS é: {dados.values.min()}') #mostra o valor minimo
print(f'O valor médio de ITENS é: {dados.values.mean()}') #mostra a média
print(f'O Desvio padrão de ITENS é: {dados.values.std()}')  #mostra o desvio padrão

print('\nVENDAS:')
dados= data_frame['VENDAS']
print(f'O valor máximo de VENDAS é: {dados.values.max()}') #mostra o valor máximo
print(f'O valor mínimo de VENDAS é: {dados.values.min()}') #mostra o valor minimo
print(f'O valor médio de VENDAS é: {dados.values.mean()}') #mostra a média
print(f'O Desvio padrão de VENDAS é: {dados.values.std()}')  #mostra o desvio padrão

print('\nVISITANTE:')
dados= data_frame['VISITANTE']
print(f'A Quantidade máxima de VISITANTE é: {dados.values.max()}') #mostra o valor máximo
print(f'A Quantidade mínima de VISITANTE é: {dados.values.min()}') #mostra o valor minimo
print(f'A Quantiddade média de VISITANTE é: {dados.values.mean()}') #mostra a média
print(f'A Quantidade de VISITANTE é: {dados.values.std()}')  #mostra o desvio padrão



#print(data_frame)

# media=[columns = ('ITENS')]
# print('A média da Coluna ITENS é:', sum(media)/len(media));
