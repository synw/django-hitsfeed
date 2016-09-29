var  num_events = 0;
var ts = new TimeSeries();
var startcounter = 0;
var i = 1;
setInterval(function() {
	var t = new Date().getTime();
	var x = 0;
	if (  num_events != 0 ) {
		var x =  num_events * 1000;
	}
	//console.log(t+' / '+x);
	ts.append(t, x);
	num_events = 0;

}, 500);

function createTimeline() {
   var chart = new SmoothieChart({
	   			millisPerPixel:68,
	   			grid:{strokeStyle:'#d7bfbf', millisPerLine:4000},
	   			timestampFormatter:SmoothieChart.timeFormatter,
	   			minValue:-500,
	   			labels:{disabled:true},
			});
   chart.addTimeSeries(ts, 
   		//{ strokeStyle: 'rgba(0, 255, 0, 1)', fillStyle: 'rgba(0, 255, 0, 0.2)', lineWidth: 2 }
		   { lineWidth:3, strokeStyle:'#00ff00', fillStyle: 'rgba(0, 255, 0, 0.2)' }
   );
   chart.streamTo(document.getElementById("hitschart"), 500);
 }
 createTimeline();