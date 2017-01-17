var twit = require('twit');
var config = require('./config.js');
var schedule = require('node-schedule');


var CronJob = require('node-cron');

var Twitter = new twit(config);

var phases = ["fckn test",
				"observe the MOON, and rotate the WHEEL. it's a half moon.", 
				"it's a new moon, babu!", 
				"First quarter fingers crossed for no wet hole!"]

var num = 0
CronJob.schedule('0 0 18 19,27,3 * *', function() {
	console.log("test");
		if(num < phases.length){
		Twitter.post('statuses/update', { status: phases[num]}, function(err, data, response) {
	  		console.log(data)
		})
		num++;
	}	
  //console.log('The answer to life, the universe, and everything!');
  
});

/*T.post('statuses/update', { status: 'hello world!' }, function(err, data, response) {
  console.log(data)
})*/
/*
*    *    *    *    *    *
┬    ┬    ┬    ┬    ┬    ┬
│    │    │    │    │    |
│    │    │    │    │    └ day of week (0 - 7) (0 or 7 is Sun)
│    │    │    │    └───── month (1 - 12)
│    │    │    └────────── day of month (1 - 31)
│    │    └─────────────── hour (0 - 23)
│    └──────────────────── minute (0 - 59)
└───────────────────────── second (0 - 59, OPTIONAL) 
*/