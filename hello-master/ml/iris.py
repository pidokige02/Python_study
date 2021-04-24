from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split

csv = pd.read_csv('./data/iris.csv')
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)

# print(trainLabel)
# print(trainData.shape)

clf = svm.SVC(gamma='auto')
clf.fit(trainData, trainLabel)   # 훈련(학습)

pred = clf.predict(testData)     # 검증(test)
score = metrics.accuracy_score(testLabel, pred)
print("score=", score)

print("===========================")
r = clf.predict([[5.6, 2.9, 3.6, 1.3]])
print("품종:", r[0])
