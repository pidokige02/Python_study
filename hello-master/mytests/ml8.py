import pandas as pd
from sklearn import metrics, svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

csv = pd.read_csv('./data/iris.csv')
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)

clf = svm.SVC(gamma='auto')
clf.fit(trainData, trainLabel)   # 훈련(학습)

pred = clf.predict(testData)     # 검증(test)
score = metrics.accuracy_score(testLabel, pred)
print("score=", score)

kscores = cross_val_score(clf, cdata, cret, cv = 5)
print("kscores=", kscores)
print("mean score =", kscores.mean())
