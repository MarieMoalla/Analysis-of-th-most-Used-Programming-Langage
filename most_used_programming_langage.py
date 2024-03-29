# -*- coding: utf-8 -*-
"""Most Used Programming Langage.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GhMFhPZCGJ-fCpTRwPoyOAeRib3_wLgX
"""

import pandas as pd 
data=pd.read_csv("stack_overflow_tags.csv")
data.info()

# Nombre de (ligne , colone)
data.shape

data['tag'].value_counts()

# 70 valeurs qui manque dans la colone total_favorites
data.isnull().sum()

d1 = data[['tag','total_views']]
d1

# Regrouper le nembre de postes delon les tags dans l'ordre ascendant 
postesPerTags = data[["tag","total_posts"]].groupby(["tag"]).mean().sort_values(by = "total_posts",ascending = False).style.background_gradient("Reds")
postesPerTags



# Regrouper le nembre de visites delon les tags dans l'ordre ascendant pour savoir quel est le sujet le plus visité
data[["tag","total_views"]].groupby(["tag"]).mean().sort_values(by = "total_views",ascending = False).style.background_gradient("Greens")

d1=data[['tag','total_posts']]
d2=data[['tag','total_views']]

d1.plot(x="tag",y="total_posts")

d2.plot(x="tag")

#on peut voir que les plus part des questions et recherche sur stack overflow est sur Python

#dans cette etape on vas faire l'analyse des languages de programmations les plus rechérche pour chaque anné depuis 2008 jusqu'a 2021 top(3)

d3= data[["tag","total_views","year"]].groupby(["year"])

for key,item in d3:
  d4 = d3.get_group(key).head(3)
  print(d4)
  d5=d3.get_group(key).head(10)
  print(d5.plot(x="tag"))

data_copy = data[["tag","total_views","year"]].copy()
data_copy

from sklearn.preprocessing import LabelEncoder
#convertir les valeur de colones de chaine de caractaire en valeurs numerique en utilisant LabelEncoder
label = LabelEncoder()
label.fit(data_copy.tag.drop_duplicates())
data_copy.tag = label.transform(data_copy.tag)
data_copy

Models Training

#on a separer la colone "year" des autre colone de data_copy
Y = data_copy.total_views
X = data_copy.drop(["total_views"], axis = 1)
X.head()

from sklearn.model_selection import train_test_split

#le paramaitre test_size utilisé pour definir la taille de donné a tester par rapport au model original
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 42)
print(X_test,'/n')
print(X_train,'/n')

print(Y_test,'/n')
print(Y_train,'/n')

from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score
import numpy as np
results = []
lr = LinearRegression()
#ajout des model à entrainer
lr.fit(X_train, Y_train)
#predict va prendre le resultat de la prediction du model a entrainer par rapport au model X utiliser pour tester
predict = lr.predict(X_test)
#comparer les valeur obtenu par rapport au model du test
score = r2_score(Y_test,predict)
print("Le nombre des vue totale prédecté:",predict)
print("le rapport moyen entre les deux resultas",score)

print('Comparaison')
df_linearRegression = pd.DataFrame({'Actual': Y_test, 'Predicted': predict})
df_linearRegression



