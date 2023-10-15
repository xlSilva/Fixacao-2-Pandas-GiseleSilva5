import pandas as pd

df_world_population = pd.read_csv('world_population.csv', index_col = 'Rank')
print(df_world_population.shape, end = '\n\n')
print(df_world_population.head(), end = '\n\n')

df_world_population.Continent.value_counts()

# Corrigindo o nome das colunas
col_dic = {
    'CCA3' : 'acronym',
    'Country/Territory' : 'country'	,
    'Capital' : 'capital',
    'Continent' : 'continent',
    '2022 Population' : '2022_population',
    '2020 Population' : '2020_population',
    '2015 Population' : '2015_population',
    '2010 Population' : '2010_population',
    '2000 Population' : '2000_population',
    '1990 Population' :	'1990_population',
    '1980 Population' :	'1980_population',
    '1970 Population' :	'1970_population',
    'Area (km²)' : 'area',
    'Density (per km²)'	: 'density',
    'Growth Rate' :	'grow_rate',
    'World Population Percentage' : 'world_population_percentage'
}

df_world_population = df_world_population.rename(col_dic, axis=1)

# Ordenando o index
df_world_population = df_world_population.sort_index()
df_world_population.set_index('country', inplace=True)
df_world_population.head()

df_world_population.sort_index(axis = 1)

print('1 - Há alguma coluna, cuja informação não seja relevante para esse projeto? é possivel descarta-la?')
#Descartando as colunas que não serão usadas
df_world_population = df_world_population.drop(['acronym','capital','grow_rate','world_population_percentage', 'density' ], axis = 1)
print(df_world_population.head(), end ='\n\n ')

print('2 - É possivel mudar os valores das colunas para que sejam de mais facil acesso?')
# mudar nomes dos continente e paises para minusculo.
df_world_population['continent'] = df_world_population['continent'].apply(lambda x : str.replace(x, ' ','_').lower())
print(df_world_population.head(), end ='\n\n ')

print('3 - Qual o pais de maior crescimento populacinal entre 1970 e 2022? \n')
# Realizar duas manipulações aritméticas necessárias na base de dados (soma, multiplicação, divisão, etc.);
sr_population_1970_2022 = (df_world_population['2022_population'] - df_world_population['1970_population'] ) / df_world_population['1970_population']
sr_pais_max = sr_population_1970_2022.idxmax()
sr_valor_max = sr_population_1970_2022.max()
print(f'Pais de maior crecimento populacional entre 1970 e 2022 é {sr_pais_max} com um crescimento de {sr_valor_max:.2%}', end = '\n\n')

print ('4 - Considerando os dados apresentados, é possivel realizar uma operação que apresente o valor aproximado do que seria os dados de 2021?\n')
df_world_population['2021_population'] = df_world_population[['2020_population','2022_population']].mean(axis = 1)
df_world_population.head()

print(f'Considerando os dados apresentados, os possiveis valores para a população mundial em 2021,\
      seriam:{df_world_population["2021_population"]}', end='\n\n')

print('5 - Qual o máximo populacional de cada país entre 1970 e 2022? \n')
max_populacional = df_world_population.loc[:, ~df_world_population.columns.isin(['continent','area'])].max(axis =1)
df_world_population['max_populacional'] = max_populacional
df_world_population.tail()
print(f'O máximo populacional que cada pais possuiu é\n{df_world_population["max_populacional"]}', end ='\n\n')

print('6 - Quantos paises tem mais de 1 bilhão de habitantes? \n')
df_world_population[df_world_population['2022_population']>1e9]

print(f'Os paises com mais de 1 bilhão de habitantes em 2022 são China e India', end = '\n\n')


print('7 - Qual o continente mais populoso em 1970 e em 2022?\n')
df_populatin_by_continent = df_world_population.groupby('continent')[['1970_population','2022_population']].max()
df_populatin_by_continent.sort_values(by='1970_population', ascending=False)
print('O continente mais populoso em 1970 era a Asia e em 2022 continua a ser a Asia. ', end = '\n\n')

# Importando o csv
df_populatin_by_continent.to_csv('populacao_continente.csv')

#Grafico de concentração populacional por continente
import matplotlib.pyplot as plt
df_populatin_by_continent.plot(title='População de Mundial de 1970 e 2022')




