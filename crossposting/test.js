/*
var sys = require('sys'), libxml = require('./libxmljs');

var doc = libxml.parseHtmlString('<root>\
	<daily-values asd="123">\
		asdasdasd\
		<total-fat units="g">65</total-fat>\
		<saturated-fat units="g">20</saturated-fat>\
		<cholesterol units="mg">300</cholesterol>\
		<sodium units="mg">2400\
		<carb units="g">300</carb>\
		<fiber units="g">25</fiber>\
		<protein units="g">50</protein>\
	</daily-values>\
</root>');

//attrs
sys.puts(doc.get('//root').children()[0].attrs()[0].value());

//text content of the node
sys.puts(doc.get('//root').children()[0].children()[0].text());

//name of the node
sys.puts(doc.get('//root').children()[0].name());

emm = events.EventEmitter;

emm.addListener('checkDaTheez', function() { sys.puts('working'); })
emm.emit('checkDaTheez');

var sys = require('sys');

process.stdio.open();
process.stdio.addListener("data", function (data) {
	for(i in JSON.parse(data)) sys.puts(JSON.parse(data)[i].somevar);
});

var sys = require('sys'), libxml = require('./lib/libxmljs');

sys.puts(libxml.parseHtmlString('text').get('//entry/link[@rel="alternate"]/@href').children()[0].text());
*/

var sys = require('sys');

sys.puts([1,2,3].join('/'));
