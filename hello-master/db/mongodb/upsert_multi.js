for (var i = 1; i <= 10; i++) {
    db.Singer.update(
        {name: 'singer' + i}, 
        {$inc: {likecnt: 1} },
        true
    )
}

db.Singer.update({likecnt: 1}, {$inc: {likecnt: 1}}, false, true);

db.Singer.find()