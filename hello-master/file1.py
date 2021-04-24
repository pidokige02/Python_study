def write_file():
    with open("a.csv", "a") as file:
        file.write("이름,성별,나이\n")
        file.write("김일수,남,14\n")
        file.write("김이수,남,24")

def write_file2(seq):
    with open("a.csv", "wa") as file:
        file.writelines(seq)

def read_file():
    with open("a.csv", "r") as file:
        for line in file:
            print("line>>", line)

def write_file3(l):
        with open("a.csv", "w+") as file:
                for i in l:
                        file.write(i)
                        file.write("\n")


# write_file()
# read_file()

lst = ['김삼수\t여\t33', '김사수\t남\t41', '김오수\t여\t77']
write_file3(lst)
