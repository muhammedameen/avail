from pandas import read_csv
import numpy as np
from fancyimpute import mice
import fancyimpute
import pandas
from pandas import DataFrame as df
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold   #For K-fold cross validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

dataset = read_csv('realdata3.csv')
modifiedData = dataset.fillna(np.NaN)
print(modifiedData.head(5))
d = modifiedData



d1 = fancyimpute.MICE().complete(d)
newd=df(data = d1, index = d.index, columns= list(d.columns))
newd.to_csv('test2.csv')
values = newd.values
outcome_var = 'BAD'
model = tree.DecisionTreeClassifier(criterion = "entropy", max_depth = 7, min_samples_split=500, min_samples_leaf=500)
predictor_var = ['LOAN', 'MORTDUE','REASON' , 'VALUE','DELINQ', 'DEROG' ,'CLAGE','Other','DELINQ', 'Office' ,'Sales', 'ProfExe']
X = values[: , range(18)[1:]]
Y = values[:,0]
model = LogisticRegression()
rfe = RFE(model, 6)
fit = rfe.fit(X, Y)
print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)




#for i in range(13)[2:]:
#	for j in range(13)[]






# model = LinearDiscriminantAnalysis()
# kfold = KFold(n_splits=3, random_state=7)
# result = cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
# print(result.mean())