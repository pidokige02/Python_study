var cur = db.Singer.find()
var i = 0;
while( cur.hasNext() ) {
    i++;
    var s = cur.next();
    if (i % 5 == 0) {
        s.likecnt = 102;
        db.Singer.save(s);
    }
    
    print(s.name);
}


cur.forEach( s => { 
    i++;
    if ( i % 5 == 0) {
        s.likecnt = 105;
        db.Singer.save(s);
    }
});


db.Singer.find({likecnt:105}, {name:1, likecnt: 1, _id: 0})