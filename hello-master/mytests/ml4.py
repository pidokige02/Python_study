from sklearn import svm, metrics

def readCsv(file, maxcnt):
    labels = []
    images = []

    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i >= maxcnt: break
            cols = line.split(",")
            labels.append(int(cols.pop(0)))
            images.append(list(map(lambda b: int(b) / 256, cols)))

    return {"labels": labels, "images": images}

train = readCsv('./data/train.csv', 2000)
test = readCsv('./data/t10k.csv', 200)

clf = svm.SVC(gamma='auto')
clf.fit(train['images'], train['labels'])

pred = clf.predict(test['images'])
print("pred=", pred)
score = metrics.accuracy_score(test['labels'], pred)
print("\n\nscore=", score)
print("-----------------------------------------")
report = metrics.classification_report(test['labels'], pred)
print(report)
