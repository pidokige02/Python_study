import pandas as pd
from sklearn import svm, metrics

xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# data = []
# label = []

# for r in xor_data:
#     data.append([r[0], r[1]])
#     label.append(r[2])

df = pd.DataFrame(xor_data)
print("cols=", df.columns)
print("cols=", list(df.columns))
print("head=", df.head)
print("shape=", df.shape)
print("len=", len(df.index))

clf = svm.SVC(gamma='auto') # support vector classification
# clf.fit(data, label)
clf.fit(df.loc[:, 0:1], df.loc[:, 2])

testset = [[0, 1], [1, 0], [2, -1]]
pred = clf.predict(testset)
print("pred>>", pred)

# 정답률 구하기
score = metrics.accuracy_score([1,1,1], pred)
print("score=", score)