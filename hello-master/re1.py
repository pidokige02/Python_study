import re
line = "Beautiful is better than ugly."
matches = re.findall("e", line)
# print(matches)

# matches2 = re.findall("beautiful", line, re.IGNORECASE)
# print(matches2)

zen2 = """Although never is often ideaXXX better than * right * now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea - - let's do more of those!"""

m = re.findall("^If", zen2, re.MULTILINE)
m2 = re.findall("idea\.", zen2, re.MULTILINE)
m22 = re.findall("idea.*", zen2, re.MULTILINE)
m3 = re.findall("idea.$", zen2, re.MULTILINE)
print(m, m2, m22, m3)
