import re

string = "123?45yy7890 hi 999 heLLo"

# a1 = re.findall("[A-z]", string)
# print(a1)

# m1 = re.findall("\d", string)
# m2 = re.findall("[0-9]{1,2}", string)
# m3 = re.findall("[1-5]{1,2}", string)

# print("m1=", m1)
# print("m2=", m2)
# print("m3=", m3)


# pattern = re.compile("[0-9]{1,3}")
pattern = re.compile("(\d{1,3})")

mm = re.findall(pattern, string)
print(mm)

for m in re.finditer(pattern, string):
    print(m.groups())
