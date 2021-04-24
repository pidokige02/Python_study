import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv('iris.csv')

# cdata = csv[:4]
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
# print(cdata)
cret = csv['Name']

trainData, testData, trainRet, testRet = train_test_split(cdata, cret)

print("train=", trainData.shape)
print("test=", testData.shape)

clf = svm.SVC(gamma='auto')
clf.fit(trainData, trainRet)
pred = clf.predict(testData)
score = metrics.accuracy_score(testRet, pred)
print("score=", score)