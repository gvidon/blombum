var
	rest = require('./lib/restler'),
	sys  = require('sys'),
	http = require('http');

var
	CATCHER_PATH = 'crossposting',
	SERVER_HOST  = 'localhost',
	SERVER_PORT  = 8001;

var crawlers = {
	'blogger': require('./crawlers/blogger'),
};

// сделать запрос по параметрам текущего обработчика и отдать
// результаты для обработки следующему
function processParams(crawler, code, catcher, P) {
	rest.post(P['url'], {
		headers: P['HEADERS'],
		data   : P['POST'],
	}).addListener('complete', function(data, response) {
		P = crawler.actions[P['parser']](data, P);
		
		if(P['url']) {
			processParams(crawler, code, catcher, P);
			return false;
		}
		
		//отправить блог движку полученные урлы
		rest.post(
			'http://' + [catcher, CATCHER_PATH, code].join('/'),
			{ data: {'url': P['entry'], 'error': (P['error'] ? P['error'] : '')} }
		).addListener('complete', function(data, response) {
				sys.puts(P['entry']);
				sys.puts(data);
		});
	});
}

http.createServer(function (request, response) {
	var data = '';
	
	request.addListener('data', function(chunk) {
		data += chunk;
		sys.puts(data);
	});
	
	request.addListener('end', function() {
		var input = JSON.parse(data);
		
		for(i in input)
			processParams(
				crawlers[input[i]['crawler']],
				input[i]['security'],
				input[i]['catcher'],
				crawlers[input[i]['crawler']].actions['auth']('', input[i]['params'])
			);
	});
}).listen(SERVER_PORT, SERVER_HOST);

sys.puts('Ready to serve, master!');
