var s1 = db.Singer.findOne({name:'singer1'})

s1.albums = [1, 2, 3]

db.Singer.save(s1)