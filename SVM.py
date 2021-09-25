# -*- coding: utf-8 -*-
"""BelajarSVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vAvL61-HRaUrjbKmViuV8QOIiHx8S7c7
"""

import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Data TA2.csv',delimiter=';')
train=df.dropna()
df.head(100)

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
LE=LabelEncoder()


train['label'].to_numpy()
x=train[['HI3','HI5','HI7','HI9','HI11']]
y=LE.fit(train['label'].to_numpy())
y=y.transform(train['label'].to_numpy())
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
model = SVC()
parameters = {
	    'kernel': ['rbf'],
	    'C':     [1, 10, 100],
	    'gamma': [0.5, 0.05,0.005]
}
grid_search = GridSearchCV(model, parameters)
grid_search.fit(xtrain,ytrain)

print(grid_search.best_params_)

from sklearn.svm import SVC

rbf=SVC(C=10,gamma=0.5,kernel='rbf')
poly=SVC(C=10,kernel='poly')
lin=SVC(C=10,kernel='linear')
# sig=SVC(kernel='sigmoid')

rbf.fit(xtrain,ytrain)
poly.fit(xtrain,ytrain)
lin.fit(xtrain,ytrain)
# sig.fit(xtrain,ytrain)

ypred_rbf=rbf.predict(xtest)
ypred_poly=poly.predict(xtest)
ypred_lin=lin.predict(xtest)
# ypred_sig=sig.predict(xtest)

from sklearn.metrics import accuracy_score

accuracy_score(ytest, ypred_rbf),accuracy_score(ytest, ypred_poly),accuracy_score(ytest, ypred_lin)

plt.plot(ypred_rbf)
plt.plot(ytest)
plt.show()

plt.plot( ypred_poly)
plt.plot(ytest)
plt.show()

plt.plot( ypred_lin)
plt.plot(ytest)
plt.show()

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import recall_score
mat = confusion_matrix(ytest, ypred_rbf)
sns.heatmap(mat.T, square=True , annot=True, fmt='d', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('true class')
plt.ylabel('predicted class')
print(classification_report(ytest, ypred_rbf))

# from sklearn.metrics import classification_report, confusion_matrix
# from sklearn.metrics import recall_score
# mat = confusion_matrix(ytest, ypred_poly)
# sns.heatmap(mat.T, square=True , annot=True, fmt='d', cbar=False)
# plt.title('Confusion Matrix')
# plt.xlabel('true class')
# plt.ylabel('predicted class')
# print(classification_report(ytest, ypred_poly))

# from sklearn.metrics import classification_report, confusion_matrix
# from sklearn.metrics import recall_score
# mat = confusion_matrix(ytest, ypred_lin)
# sns.heatmap(mat.T, square=True , annot=True, fmt='d', cbar=False)
# plt.title('Confusion Matrix')
# plt.xlabel('true class')
# plt.ylabel('predicted class')
# print(classification_report(ytest, ypred_lin))

# Commented out IPython magic to ensure Python compatibility.
from pylab import rcParams
# %matplotlib inline
from matplotlib import rcParams
from matplotlib.cm import rainbow




def plot_correlation(df):
    '''
    plot correlation's matrix to explore dependency between features 
    '''
    # init figure size
    rcParams['figure.figsize'] = 15, 20
    fig = plt.figure()
    sns.heatmap(df.corr(), annot=True, fmt=".2f")
    plt.title('correlation map')
    plt.show()
    fig.savefig('corr.png')
# plot correlation & densities
plot_correlation(df)

test=[[	2.85,	1.67,	3.19,	2.27,	2.26]]
pred_rbf = rbf.predict(test)
print('Hasil prediksi:', LE.inverse_transform(pred_rbf)) 

test1=[[	6.50,	1.33,	3.66,	2.22,	0.82]]
pred_rbf = rbf.predict(test1)
print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

test2=[[4.06,	1.55,	1.19,	1.21,	0.63]]
pred_rbf = rbf.predict(test2)
print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

test3=[[4.27,	2.09,	1.09,	1.23,	0.57]]
pred_rbf = rbf.predict(test3)
print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

test4=[[4.2,	2.06,	0.93,	1.26,	0.64]]
pred_rbf = rbf.predict(test4)
print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test5=[[4.06,	1.95,	1.2,	1.29,	0.44]]
# pred_rbf = rbf.predict(test5)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test6=[[4.13,	1.94,	1.18,	1.27,	0.62]]
# pred_rbf = rbf.predict(test6)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test7=[[4.1,	1.85,	1.23,	1.33,	0.53]]
# pred_rbf = rbf.predict(test7)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test8=[[4.09,	1.86,	1.01,	1.35,	0.46]]
# pred_rbf = rbf.predict(test8)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test9=[[4.11,	1.98,	1.09,	1.35,	0.46]]
# pred_rbf = rbf.predict(test9)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test10=[[4.14,	2,	1.08,	1.14,	0.51]]
# pred_rbf = rbf.predict(test10)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test11=[[3.93,	1.96,	0.98,	1.06,	0.4]]
# pred_rbf = rbf.predict(test11)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test12=[[4.23,	2.01,	1.15,	1.04	,0.5]]
# pred_rbf = rbf.predict(test12)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test13=[[4.06,	2.09,	1.17,	1.24,	0.73]]
# pred_rbf = rbf.predict(test13)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test14=[[4.21,	2.02,	1.23,	1.29,	0.66]]
# pred_rbf = rbf.predict(test14)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test15=[[4.51,	1.7	,1.07,	1.19,	0.63]]
# pred_rbf = rbf.predict(test15)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test16=[[4.5,	1.76,	1.01,	1.25,	0.54]]
# pred_rbf = rbf.predict(test16)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test17=[[4.37,	1.85,	1.19,	1.04,	0.48]]
# pred_rbf = rbf.predict(test17)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test18=[[4.59,	1.54,	1.33,	1.16,	0.59]]
# pred_rbf = rbf.predict(test18)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

# test19=[[4.4,	1.64,	1.05,	0.83,	0.84]]
# pred_rbf = rbf.predict(test19)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))
# #hairdyer

# test20=[[5.25,	2.47,	1.74,	1.14,	0.83]]
# pred_rbf = rbf.predict(test20)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))
# #HairdryerBlenderKipas

# test21=[[4.91,	2.39,	1.66,	1.18,	0.46]]
# pred_rbf = rbf.predict(test21)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))
# #HairdryerPemanas Ai

# test22=[[5.01	,2.37	,1.79,	1.12,	0.6]]
# pred_rbf = rbf.predict(test22)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))
# #HairdryerPemanas Ai

# test23=[[5.47,	2.76,	1.69,	1.05,	0.75]]
# pred_rbf = rbf.predict(test23)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))
# #HairdryerPemanas Ai

# test24=[[5.26,	2.99,	1.67,	1.64,	0.6]]
# pred_rbf = rbf.predict(test24)
# print('Hasil prediksi:', LE.inverse_transform(pred_rbf))
# #HairdryerPemanas Ai

sns.pairplot(df, hue="label")

X_ = train[['HI3', 'HI5']].to_numpy()
y_ = LE.fit(train['label'].to_numpy())
y_=y_.transform(train['label'].to_numpy())

svc = SVC(kernel='linear', C=100).fit(X_,y_)
rbf_svc = SVC(kernel='rbf', C=100, gamma=.05).fit(X_,y_)

x_min, x_max = X_[:,0].min()-1, X_[:,0].max()+1
y_min, y_max = X_[:,1].min()-1, X_[:,1].max()+1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02), np.arange(y_min, y_max, .02))

for i, clf in enumerate ((svc, rbf_svc)):
  Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
  Z = Z.reshape(xx.shape)

  plt.contourf(xx, yy, Z, cmap=plt.cm.Accent, alpha=0.3) 

  plt.scatter(X_[:,0], X_[:,1], c=y_ , cmap=plt.cm.Accent)
  plt.xlim(xx.min(), xx.max())
  plt.ylim(yy.min(), yy.max())
  plt.xticks(())
  plt.yticks(())
plt.show()

from sklearn.externals import joblib
joblib.dump(SVC, 'ModelSVM.pkl')

hh=joblib.load('ModelSVM.pkl')

test88=[[	2.85,	1.67,	3.19,	2.27,	2.26]]
pred_rbf = rbf.predict(test88)
print('Hasil prediksi:', LE.inverse_transform(pred_rbf))

