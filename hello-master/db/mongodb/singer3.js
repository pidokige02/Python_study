db.Singer.update(
                    {name: 'singer1'}, 
                    {
                        $set: {hitsongs: [
                                {title: '24/7', albumId: 1},
                                {title: '222', albumId: 2}
                            ]}
                    }
                )