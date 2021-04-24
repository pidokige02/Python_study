import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("./data/mushroom.csv")
# print(df.shape)
# print(df.head)

allLabel = []
allData = []  # [[s,t,t]]

for rowidx, row in df.iterrows():         # cf. enumerate
    allLabel.append(row.iloc[0])
    ords = []
    for c in row.iloc[1:]:
        ords.append(ord(c))

    allData.append(ords)

trainData, testData, trainLabel, testLabel = train_test_split(allData, allLabel)

clf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=4096)       
clf.fit(trainData, trainLabel)   # 훈련(학습)

pred = clf.predict(testData)     # 검증(test)
score = metrics.accuracy_score(testLabel, pred)
print("score=", score)

report = metrics.classification_report(testLabel, pred)
print(report)
