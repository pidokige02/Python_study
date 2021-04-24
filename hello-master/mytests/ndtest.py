from collections import namedtuple

t1 = (1, 'name1')
print(t1, type(t1))
print("%d %s" % t1)

song = namedtuple('Song', 'songno title likecnt')
s1 = song(123, '만남', 100)
s2 = song(songno=222, title='강남스타일', likecnt=200)
print("FFFFFFFFFFF>>", s2._fields)
s3 = song._make([333, 'Radio ga ga', 300])
d1 = s1._asdict()
print(d1, type(d1))

s2 = s2._replace(likecnt=201)

for s in [s1, s2, s3]:
    print("songno=%d, title=%s, like: %d" % s, getattr(s, 'title'))