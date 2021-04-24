import re

string = "aaaaaaa<hr>This</hr><html>"

# pattern = re.compile("<(.*)>")        
pattern = re.compile("<(.{1,2})>")        

mm = re.findall(pattern, string)
print(mm)

# for m in re.finditer(pattern, string):
#     print(m.groups(1))
