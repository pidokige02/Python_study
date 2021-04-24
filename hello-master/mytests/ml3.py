import struct, math

def drawImageData(imgdata, label):
    for j, x in enumerate(imgdata):
        if j % 28 == 0:
            print("\n")

        print('{:4s}'.format(str(x)), end='')

    print("\nlabel=", label)

def writeCsvFile(name):
    labelFile = open("./data/" + name + "-labels-idx1-ubyte", "rb")
    imageFile = open("./data/" + name + "-images-idx3-ubyte", "rb")
    csvFile = open("./data/" + name + ".csv", "w", encoding="utf-8")

    # unpack(B: unsigned char, I: unsigned int)
    magicNo, labelCnt = struct.unpack(">II", labelFile.read(8))  # unsigned int 4B * 2개, magic no. & count
    print("lll=", magicNo, labelCnt)
    magicNo, imageCnt = struct.unpack(">II", imageFile.read(8))  # unsigned int 4B * 2개, magic no. & count
    print("iii=", magicNo, imageCnt)

    rows, cols = struct.unpack(">II", imageFile.read(8))
    print("rows, cols =", rows, cols)
    pixels = rows * cols
    print("pixels=", pixels, math.sqrt(pixels))

    for i in range(labelCnt):
        # if i > 1000: break

        label = struct.unpack("B", labelFile.read(1))[0]
        print(i, "label=", label)
        # imgdata = imageFile.read(pixels)
        imgdata = list(map(lambda b: str(b), imageFile.read(pixels)))
        if i == 0:
            drawImageData(imgdata, label)

        csvFile.write(str(label) + ",")
        csvFile.write(",".join(imgdata) + "\r\n")

    labelFile.close()
    imageFile.close()
    csvFile.close()


writeCsvFile('train')
writeCsvFile('t10k')
