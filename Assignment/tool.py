	
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
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import _tree
import graphviz

dataset = read_csv('realdata3.csv')
modifiedData = dataset.fillna(np.NaN)
print(modifiedData.head(5))
d = modifiedData



d1 = fancyimpute.MICE().complete(d)
newd=df(data = d1, index = d.index, columns= list(d.columns))
newd.to_csv('test2.csv')


#criterion = "entropy", max_depth = 7, min_samples_split=500, min_samples_leaf=500
outcome_var = 'BAD'
model = tree.DecisionTreeClassifier(criterion = "entropy", max_depth =12 , min_samples_split=500, min_samples_leaf=200)
predictor_var = ['LOAN', 'MORTDUE','REASON' , 'VALUE','DELINQ', 'DEROG' ,'CLAGE','Other','DELINQ', 'Office' ,'Sales', 'ProfExe']


X_train, X_test, y_train, y_test = train_test_split(newd[predictor_var], newd[outcome_var], test_size=0.33, random_state=42)
#Fit the model2
model.fit(X_train,y_train)

#Make predictions on training set:
predictions = model.predict(X_test)

#Print accuracy
accuracy = metrics.accuracy_score(predictions,y_test)
print ("Accuracy : %s" % "{0:.3%}".format(accuracy))

dot_data=export_graphviz(model, out_file="abc", feature_names=predictor_var, class_names='BAD', filled=True, rounded=True)
graph = graphviz.Source(dot_data)
graph



def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    print("def tree({}):".format(", ".join(feature_names)))

    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print("{}if {} <= {}:".format(indent, name, threshold))
            recurse(tree_.children_left[node], depth + 1)
            print("{}else:  # if {} > {}".format(indent, name, threshold))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print("{}return {}".format(indent, tree_.value[node]))

    recurse(0, 1)
tree_to_code(model , predictor_var)