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

