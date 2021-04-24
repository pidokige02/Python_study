import random
from pprint import pprint
data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

pprint(data)

sum1 = 0
sum2 = 0
for i, l in enumerate(data['C']):
    print(i, l, l[i], l[-i -1], l[i] + l[-i - 1])
    sum1 += l[i] + l[-i - 1]

print("sum1>>", sum1)

result = {}
sumr = {}
for k, v in data.items():
    sums = sum([l[i] + l[-i - 1] for i, l in enumerate(v)])
    sumr[k] = sums
    result[sums] = k
    print(">>", sums)

print(result)
# print("min>>", result.values(), min(result.values()))
print("min>>", result.keys(), min(result.keys()))

print(result[min(result.keys())])
print("-----------------------------------------------")

r = sorted(sumr.items(), key=lambda x: x[1])
print(r, "::", r[0][0])

minx = min(sumr, key=lambda x: sumr[x])
miny = min(sumr.items(), key=lambda y: y[1])[0]
print("minx=", minx, miny)

print("-----------------------------------------------", sumr)
q = dict((v, k) for k, v in sumr.items())
print(q)