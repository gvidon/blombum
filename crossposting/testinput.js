var	sys = require('sys');

process.stdio.open();

var c='';

process.stdio.addListener('data', function (data) {
	c+=data;
	sys.puts(data);
	sys.puts(c);
	
	if(data=='A')
		process.stdio.close()
});

