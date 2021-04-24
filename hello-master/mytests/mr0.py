import sys
from pprint import pprint

l = [
    (2001, 23),
    (2002, 7),
    (2002, -12),
    (2001, 21),
    (2003, 20),
    (2005, 13),
    (2003, 3),
    (2005, -2),
    (2003, 22),
    (2001, -3)
]

pprint(l)
print("---------------------------- sort")
l.sort()
pprint(l)

ret = {}
oldkey = None
for i in l:
    (key, val) = i
    if oldkey != key:
        oldkey = key
        ret[key] = [val]
    
    else:
        oldval = ret.get(key)
        oldval.append(val)
        
print("------------------------------------- ret")
pprint(ret)

print("---------------------------------- result")
for k,v in ret.items():
    print("%s\t%s" % (k, max(v)))
