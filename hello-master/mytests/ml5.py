from sklearn import svm, metrics
from sklearn.externals import joblib
from pathlib import Path


def readCsv(file, maxcnt):
    labels = []
    images = []

    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i >= maxcnt:
                break
            cols = line.split(",")
            labels.append(int(cols.pop(0)))
            images.append(list(map(lambda b: int(b) / 256, cols)))

    return {"labels": labels, "images": images}


test = readCsv('./data/t10k.csv', 500)

pklFile = "mnist.pkl"
clf = None
print(">>>>>>>>", Path(pklFile).exists())
if Path(pklFile).exists():
    clf = joblib.load(pklFile)

if not clf:
    print("Not exists clf!!")
    train = readCsv('./data/train.csv', 2000)

    clf = svm.SVC(gamma='auto')
    clf.fit(train['images'], train['labels'])
    joblib.dump(clf, pklFile)


pred = clf.predict(test['images'])
print("pred=", pred)
score = metrics.accuracy_score(test['labels'], pred)
print("\n\nscore=", score)
print("-----------------------------------------")
report = metrics.classification_report(test['labels'], pred)
print(report)
