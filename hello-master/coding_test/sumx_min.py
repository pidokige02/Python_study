data = {
    "A": [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B": [
        [2, -7,  2, -2,  0],
        [1,  8,  2,  2, -2],
        [6, -2,  5, -2,  5],
        [-4, 9, -5, -9, -7],
        [8,  0, -9,  2, -7]
    ],

    "C": [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

# print(data.items())
# {
#     A: 00,
#     B: 00,
#     C:9
# }

result = {}
for k, dlist in data.items():
    sum = 0
    for i, l in enumerate(dlist):
        sum += l[i] + l[-i - 1]
    result[k] = sum

# print(result)

mk = ''

# mk = min(result, key=lambda x: result[x])
mk = min(result.items(), key=lambda x: x[1])[0]

# mv = min(result.values())
# print(mv)
# for k, v in result.items():
#     if v == mv:
#         mk = k
#         break

# mv = 100000000000
# for k, v in result.items():
#     if v < mv:
#         mv = v
#         mk = k
#     print(k, v, mk, mv)

# print("-----------------------------------")
print("result is", mk)
