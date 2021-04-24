import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("./data/mushroom.csv")
allLabel = []
allData = []
# print(df.head)

for rowidx, row in df.iterrows():
    # print("rowidx=", rowidx)
    # print("--------------------", list(row.ix[1:]))
    # print(row)
    # if rowidx > 20: break

    allLabel.append(row.iloc[0])

    ords = []
    for c in row.iloc[1:]:
        ords.append(ord(c))
    
    allData.append(ords)
    print("--------------------------", rowidx)

for i in range(len(allData)):
    print(i, allLabel[i], allData[i])
    if i > 1:
        break

trainData, testData, trainLabel, testLabel = train_test_split(allData, allLabel)

clf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=4096)
clf.fit(trainData, trainLabel)

pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)
print("score=", score)
report = metrics.classification_report(testLabel, pred)
print(report)
