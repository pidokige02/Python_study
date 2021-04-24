import timeit
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from pprint import pprint

df = pd.read_csv("./data/mushroom.csv")
allLabels = []
allData = []
attributes = []
print(df.head)

for rowidx, row in df.iterrows():
    # print("rowidx=", rowidx)
    # print("--------------------", list(row.ix[1:]))
    # print(row)
    # if rowidx > 2: break

    exdata = []
    l, data = row.ix[0], row.ix[1:]
    allLabels.append(l)
    for i, k in enumerate(data):
        if rowidx == 0:
            attr = {"dic": {}, "cnt": 0}
            attributes.append(attr)
        else:
            attr = attributes[i]

        d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if k in attr['dic']:
            idx = attr['dic'][k]
        else:
            idx = attr['cnt']
            attr['dic'][k] = idx
            attr['cnt'] += 1

        d[idx] = 1
        exdata += d

    allData.append(exdata)

for i in range(len(allData)):
    print(i, allLabels[i], allData[i])
    if i > 1: break

trainData, testData, trainLabel, testLabel = train_test_split(allData, allLabels)

clf = RandomForestClassifier(n_estimators=100, n_jobs = -1)
clf.fit(trainData, trainLabel)

pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)
print("score=", score)

end = timeit.default_timer()
print("Elapsed time is", (end - start), "ms.")
