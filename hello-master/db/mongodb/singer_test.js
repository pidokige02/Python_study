var s2 = db.Singer.findOne({name: 'singer2'});

s2.hitsongs = [
                    {title: '222-1', albumId: 1},
                    {title: '222-2', albumId: 2}
             ];
                                
db.Singer.save(s2)                                