import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin\\breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
df.to_csv('breast-cancer-wisconsin\\breast-cancer-wisconsin_modified.csv')

X = np.array(df.drop(['class'], 1)) #features
y = np.array(df['class']) #labels/class

#cross_validation or model_selection
X_test, X_train, y_test, y_train = model_selection.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accurancy = clf.score(X_test, y_test)
print(accurancy)

example_measures = np.array(
    [[4, 2, 1, 1, 1, 2, 3, 2, 1], [9, 2, 4, 2, 3, 2, 3, 2, 8]])
example_measures = example_measures.reshape(len(example_measures),-1)
prediction = clf.predict(example_measures)
print(prediction)
