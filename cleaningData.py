#importando as bibliotecas necessarias para tratamento do dado
import pandas as pd
import numpy as np
url = ''
#Criando um Dataframe
df = pd.read_csv(url)
#avaliando a quantidade de registros nulos por coluna
print df.isnull().sum()


def nanAsZero(f_in):
	#f_in é o parâmetro referente ao arquivo CSV 
	#função que irá retornar um dataframe, no qual todos os valores faltantes serão substituídos por Zero
	
	#Criando um Dataframe
	df = pd.DataFrame(f_in)
	#substituindo os valores do dataframe por Zero
	df = df.fillna(0)
	#retornando o dataframe tratado
	return df

def nanAsMean(f_in,column):
	#f_in é o parâmetro referente ao arquivo CSV 
	#função que irá retornar um dataframe, no qual todos os valores faltantes serão substituídos por Zero
	
	#Criando um Dataframe
	df = pd.DataFrame(f_in)
	#substituindo os valores do dataframe por Zero
	df[column] = df[column].fillna(np.mean(df[column]))
	#retornando o dataframe tratado
	return df




def dropNullValues(f_in,column):
	#parametros 
	#f_in... arquivo de entrada para gerar o dataframe
	#column... coluna que não pode ter valores nulos
	#esta função irá apagar todas as linhas do dataframe que contenham valores nulos
	
	#criando o dataframe
	dfnull = pd.DataFrame(f_in)
	#substituindo revomendo as linhas que contém valores nulos para uma coluna específica
	dfnull = dfnull[pd.notnull(dfnull[column])]
	return dfnull

def dropcol(f_in,columns):
	dfcol = pd.DataFrame(f_in)
	fieldToDrop = [columns]
	for col in fieldToDrop:
		dfcol = dfcol.drop(col, axis = 1)
	return dfcol

