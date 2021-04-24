from sklearn import svm, metrics
import pandas as pd

xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

df = pd.DataFrame(xor_data)

# print(df.loc[:, 0:1])
# print("--------------------")
# print(df.loc[:, 2])

clf = svm.SVC(gamma='auto')
clf.fit(df.loc[:, 0:1], df.loc[:, 2])

testset = [[0,1]]
testset = [[0, 1], [1, 0], [1, 1], [2, -1], [3, 1]]
pred = clf.predict(testset)
print("pred=", pred)
# score = metrics.accuracy_score([1], pred)
score = metrics.accuracy_score([1, 1, 0, 1, 1], pred)
print("score=", score)

while True:
    cmd = input("Input x y>> ")
    if not cmd: break
        
    x, y = cmd.split(' ')
    t = [[int(x), int(y)]]
    p = clf.predict(t)[0]
    print("pred=", "참" if p == 1 else '거짓')

# print("head=", df.head)
# print("shape=", df.shape)
# print("colums=", list(df.columns))
# print("nrow=", len(df.index))
