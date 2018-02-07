import pandas as pd
from sklearn import tree

def fraud_predict(url_train,url_test):
	#le os arquivos e os transforma em dataframe 
	df = pd.read_csv(url_train,sep=";")
	df_test = pd.read_csv(url_test,sep= ";")
	#atribui o algoritmimo de classificacao a variavel clf
	clf = tree.DecisionTreeClassifier()
	#atribui os campos do dataframe para a variavel x
	x = df.iloc[0:, 0:7]
	#atribui os campos do dataframe para a variavel y
	y = df.iloc[0:, 7:8]
	
	#treina o algoritmo com as variaveis x e y
	clf = clf.fit(x,y)
	#faz a predicao do arquivo passado na entrada... url_test
	prd = clf.predict(df_test)
	
	#retorna a variavel prd
	
	return prd