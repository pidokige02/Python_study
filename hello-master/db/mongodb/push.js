var k3 = {name:'singer3'}
// db.Singer.update(k3, {
//     $push: {albums: 10}
// })

var arr = [];
for (var i = 0; i <= 10; i++) {
    arr[i] = 100 + i;
}

db.Singer.update(k3, {
    //$push: {albums: {$each: [100, 102, ...]} }
    $push: {albums: {$each: arr} }
})

db.Singer.update({name:'singer3'}, {
    $pull: {albums: 105}
})


// arr

db.Singer.findOne({name:'singer3'})
db.Singer.find({name:'singer3'})