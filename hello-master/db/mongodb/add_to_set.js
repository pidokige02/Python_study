
//db.Song.findOne({title:'노래1'})
db.Singer.findOne()

db.Song.update({title:'노래1'}, 
                {
                    $addToSet: {scores: {$each: [68,69]}}
                }
)