from sklearn import svm, metrics
import pandas as pd
from sklearn.externals import joblib
from pathlib import Path
from sklearn.model_selection import GridSearchCV

def readCsv(file, maxcnt):
    labels = []
    images = []
    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i >= maxcnt:
                break
            cols = line.split(",")
            labels.append(int(cols.pop(0)))      # 첫번째 자리가 label
            images.append(list(map(lambda b: int(b) / 256, cols)))  # 실수 벡터화
    return {"labels": labels, "images": images}


train = readCsv('./data/train.csv', 1000)   # 학습용 데이터가 많아질수록 스코어 상승!
test = readCsv('./data/t10k.csv', 1000)

# clf = svm.SVC(gamma='auto')
# clf = svm.SVC(C=100, cache_size=200, class_weight=None, coef0=0.0,
#               decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
#               max_iter=-1, probability=False, random_state=None, shrinking=True,
#               tol=0.001, verbose=False)

# find best params
params = [
    {"C": [1, 10, 100, 1000], "kernel": ['linear']},
    {"C": [1, 10, 100, 1000], "kernel": ['rbf'], "gamma": [0.01, 0.001, 0.0001]},
]
clf = GridSearchCV(svm.SVC(), params, n_jobs=-1, cv=3, iid=True)

clf.fit(train['images'], train['labels'])

print("machine=", clf.best_estimator_)

# test -------------------------
pred = clf.predict(test['images'])

score = metrics.accuracy_score(test['labels'], pred)
print("\n\nscore=", score)

print("-----------------------------------------")
report = metrics.classification_report(test['labels'], pred)
print(report)
