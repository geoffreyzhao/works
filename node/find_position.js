var mongoose = require('mongoose');
var db = mongoose.createConnection('localhost','abc');

db.on('error', console.error.bind(console, 'connection error'));
db.on('open', function(){

    console.log("connected");
    var positionSchema = mongoose.Schema({
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
    });

    var positionModel = mongoose.model('position_info', positionSchema);
    //console.log(positionModel);

    //positionModel.findOne({'name': 'web前端'}, function(err, position){
    //    console.log("find finished");
    //    if (err) console.log('err');
    //});
});