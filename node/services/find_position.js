var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var db = mongoose.connect('mongodb://localhost/works');

var positionSchema = new Schema({
    name: String,
    site: String,
    datetime: Date,
    companyName: String,
    salaryMin: Number,
    salaryMax: Number,
    workExperience: String,
    education: String,
    companyType: String,
    companyResource: String,
    timestamp: { type: Date, default: Date.now }
}, {
    collection: 'position_info'
});

var positionModel = mongoose.model('PositionInfo', positionSchema);

positionModel.find({}, function(err, positions){
    if (err) {
        console.log('err');
    } else {
        //console.log(positions);
        for (var i = 0; i < positions.length; i++) {
            console.log(i + ": " + positions[i].name);
        }
    }
});