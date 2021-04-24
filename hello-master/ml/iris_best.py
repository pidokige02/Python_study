from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

csv = pd.read_csv('./data/iris.csv')
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)

isFinding = False

# 1. 최적의 매개변수 찾기
if isFinding:
    params = [
        {"C": [10, 100, 150], "kernel": ['linear']},
        {"C": [10, 100, 150], "kernel": ['rbf'], "gamma": [0.01, 0.001, 0.0001], "random_state": [2000, 4096]},
    ]
    clf = GridSearchCV(svm.SVC(), params, n_jobs=-1, cv=3, iid=True)

else:
    clf = svm.SVC(C=100, cache_size=200, class_weight=None, coef0=0.0,
                  decision_function_shape='ovr', degree=3, gamma=0.01, kernel='rbf',
                  max_iter=-1, probability=False, random_state=2000, shrinking=True,
                  tol=0.001, verbose=False)

clf.fit(trainData, trainLabel)   # 훈련(학습)

if isFinding:
    print("machine=", clf.best_estimator_)

pred = clf.predict(testData)     # 검증(test)
score = metrics.accuracy_score(testLabel, pred)
print("score=", score)

print("-----------------------------------------")
report = metrics.classification_report(testLabel, pred)
print(report)
