db.Song.update({title:'노래1'}, 
               {
                   $pull: {scores: 68}
               })