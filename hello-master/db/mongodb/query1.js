// db.Song.findOne({title: '노래1'}, {title: 1, _id: 0})

// db.Song.find({ title: /^노래3+1$/ })

db.food.insert({ _id: 1, fruit: ['apple', 'banana', 'peach'] })
db.food.insert({ _id: 2, fruit: ['apple', 'orange', 'melon'] })
db.food.insert({ _id: 3, fruit: ['cherry', 'peach'] })

db.food.find({ fruit: 'apple' })

db.food.find({ fruit: {$all: ['banana', 'apple']} })

db.food.find({ "fruit.2": 'peach' })

db.food.find({ fruit: {$size: 3} }) 