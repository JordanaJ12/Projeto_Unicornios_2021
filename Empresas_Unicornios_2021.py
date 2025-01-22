# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:00:49 2025

@author: jojoj
"""

#Importando as bibliotecas:
# Importar as libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
#%%

#Lendo a base de dados:
Base_dados = pd.read_csv('Startups+in+2021+end.csv')

#Verifica dimensão:
Base_dados.shape

#Primeiros registros:
Base_dados.head()

#%%
#Colunas:
Base_dados.columns

#Renomear:
# Renomear
Base_dados.rename( columns={
    'Unnamed: 0' : 'Id',
    'Company' : 'Empresa',
    'Valuation ($B)' : 'Valor ($)',
    'Date Joined' : 'Data de Adesão',
    'Country' : 'Pais',
    'City' : 'Cidade',
    'Industry': 'Setor',
    'Select Investors': 'Investidores',
}, inplace=True)
#%%
# Verificar Tipo do informação:
Base_dados.info()

#Verificar campos nulos:
Base_dados.isnull().sum()

#%%

#Gráfico:
plt.figure(figsize=(15,6))
plt.title('Analisando Campos Nulos')
sns.heatmap(Base_dados.isnull(), cbar=False);#; tira a legenda da figura em cima do gráfico

#%%
#Campos unicos:
Base_dados.nunique()

#Valores unicos em 'setor':
Base_dados['Setor'].nunique();

#Valores Unicos - Rank
Base_dados['Setor'].value_counts()

#Valores Unicos - Rank em porcentagem:
Base_dados['Setor'].value_counts(normalize= True)

#%%
#Fazendo um gráfico de barra:
plt.figure( figsize=(15,6) )
plt.title('Análise dos Setores')
plt.bar(Base_dados['Setor'].value_counts().index, Base_dados['Setor'].value_counts())
plt.xticks(rotation=45, ha='right');#rotaciona a legenda X em 45 graus para a direita

#%%
# Transforma a porcentagem em casas decimais e reduz para uma casa após a virgula
Analise = round( Base_dados['Pais'].value_counts( normalize=True ) * 100, 1 )

Analise

#%%
#Gráfico de pizza dos paises:
plt.figure(figsize=(15,6))
plt.title('Análise de Países Geradores de Unicórnios')
plt.pie(
    Analise,
    labels= Analise.index,
    shadow= True,
    startangle= 90,
    autopct= '%1.1f%%'

);

#%%
#Fazendo uma limpeza no gráfico de pizza:
#Apenas os 4 paises mais geradores de unicornios:
#Gráfico de pizza dos paises:
plt.figure(figsize=(15,6))
plt.title('Análise de Países Geradores de Unicórnios')
plt.pie(
    Analise.head(4),
    labels= Analise.index[0:4],
    shadow= True,
    startangle= 90,
    autopct= '%1.1f%%'

);

#%%
#Conversão para data:
Base_dados['Data de Adesão'] = pd.to_datetime(Base_dados['Data de Adesão'])

Base_dados['Data de Adesão'].head()

#%%
#Extrair o mês e ano:
Base_dados['Mes'] = pd.DatetimeIndex(Base_dados['Data de Adesão']).month
Base_dados['Ano'] = pd.DatetimeIndex(Base_dados['Data de Adesão']).year

Base_dados.head()

#%%

#Agrupar as informações pelo pais, ano e mês selecionando apenas a coluna Id:
Base_dados.groupby(by = ['Pais', 'Ano', 'Mes', 'Empresa']).count()['Id']

#Transformando em uma tabela Análitica:
Analise_Agrupada = Base_dados.groupby(by = ['Pais', 'Ano', 'Mes', 'Empresa']).count()['Id'].reset_index()

Analise_Agrupada

#%%
#Localizar apenas os dados do Brasil:

Analise_Agrupada.loc[
    Analise_Agrupada['Pais'] == 'Brazil'
]

#Retirar $ dos valores e converter para número flutuante:
#apply é usado junto com lambda para realizar algum cálculo dentro de uma coluna ou linha de um dataframe(usado no pandas):

Base_dados['Valor ($)'] = pd.to_numeric( Base_dados['Valor ($)'].apply( lambda Linha: Linha.replace('$', '') ) )
Base_dados.head()


#%%
# Agrupar o Paises com maiores valores(maior para o menor)
Analise_Pais = Base_dados.groupby(by = ['Pais']).sum(numeric_only=True)['Valor ($)'].reset_index().sort_values('Valor ($)',ascending=False)
Analise_Pais.head(10)

#Colocando em um gráfico de linha:
plt.figure(figsize=(15,6))
plt.title('Análise do valor do pais')
plt.plot(Analise_Pais['Pais'], Analise_Pais['Valor ($)'])
plt.xticks(rotation= 45, ha='right');