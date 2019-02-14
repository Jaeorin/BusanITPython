<!DOCTYPE HTML>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<title>temperature, humidity</title>
	<link rel="stylesheet" href="//code.jquery.com/mobile/1.4.3/jquery.mobile-1.4.3.min.css" />
	<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
	<script src="//code.jquery.com/mobile/1.4.3/jquery.mobile-1.4.3.min.js"></script>
	<script src="//cdnjs.cloudflare.com/ajax/libs/highcharts/4.0.4/highcharts.js">
</script>
	<script>
		var chart; //temperature
		var chart2; //humudity
		var pollUri="/events";
	function pollEvent(){
		$.getJSON(pollUri,
				function(data){
					var t = new Date();
					t.setHours(t.getHours() + 9);
					chartAddPoint([t.getTime(), Number(data.temperature)]);
					chart2AddPoint([t.getTime(), Number(data.humidity)]);
				}
		);
		setTimeout('pollEvernt()', 5000);
	}
	pollEvent();
	function chartAddPoint(tval){
		var series = chart.series[0],
		shift = series.data.length > 20;
		chart.series[0].addPoint(eval(tval), true, shift);
	}
	function chart2AddPoint(hval){
		var series2 = chart2.series[0]
		shift2 = series2.data.length > 20;
		chart2.series[0].addPoint(eval(hval), true, shift2);
	}
	$(function(){
		//temperature
		chart = new Highcharts.Chart({
			chart:{ renderTo: 'temp', defaultSeriesType: 'spline' },
			title:{ text: 'real time temperatuer' },
			xAxis:{ type: 'datetime', tickPixelInterval: 120, maxZoom: 20 * 1000 },
			yAxis:{ minPadding: 0.2, maxPadding: 0.2, title: { text: 'temperature ( C )', margin: 20 } },
			series:[{ name: 'temperature', data: [] }]
		});
		//humidity
		chart2 = new Highcharts.Chart({
			chart:{ renderTo: 'humi', defaultSeriesType: 'spline' },
			title:{ text: 'real time humidity' },
			xAxis:{ type: 'datetime', tickPixelInterval: 120, maZoom: 20 * 1000 },
			yAxis:{ minPadding: 0.2, maxPadding: 0.2, title: { text: 'humidity ( % )',margin: 20 }},
			series: [{ name: 'humidity', data: [] }]
		});
	});
	</script>
</head>
<body>
	<div id="temp" style="width: 100%; height: 300px; margin-left:-5px;"></div>
	<div id="humi" style="width: 100%; height: 300px; margin-left:-5px;"></div>
</body>
</html>
