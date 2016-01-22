/**
 * Created by shuaigeng.zhao on 2016/1/21.
 */

var express = require('express');
var mongoose = require('mongoose');

mongoose.connect("mongodb://localhost/works", function(err){
    if (err) {
        console.log("Mongo数据库连接失败");
    }
});

var positionSchema = new mongoose.Schema({
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

var posiitonModel = mongoose.model("Position", positionSchema);

function Position(position) {
    this.name = position.name;
    this.site = position.site;
    this.datetime = position.datetime;
    this.companyName = position.companyName;
    this.salaryMin = position.salaryMin;
    this.salaryMax = position.salaryMax;
    this.workExperience = position.workExperience;
    this.education = position.education;
    this.companyType = position.companyType;
    this.companyResource = position.companyResource;
    this.timestamp = position.timestamp;
}

Position.prototype.save = function(){

}