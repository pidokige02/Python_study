db.Singer.update({name:'singer1'}, 
        {$unset: {likecnt: 1}}
)