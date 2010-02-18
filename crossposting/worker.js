var
	rest = require('./lib/restler'),
	sys  = require('sys'),
	http = require('http');

var
	RESULT_CATCHER_URL = 'http://localhost:8000/crossposting/',
	SERVER_PORT        = 8001;

var crawlers = {
	'blogger': require('./crawlers/blogger'),
};

// сделать запрос по параметрам текущего обработчика и отдать
// результаты для обработки следующему
function processParams(crawler, code, P) {
	rest.post(P['url'], {
		headers: P['HEADERS'],
		data   : P['POST'],
	}).addListener('complete', function(data, response) {
		P = crawler.actions[P['parser']](data, P);
		
		if(P['url']) {
			processParams(crawler, code, P);
			return false;
		}
		
		//отправить блог движку полученные урлы
		rest.post(
			RESULT_CATCHER_URL + code,
			{ data: {'url': P['entry']} }
		).addListener('complete', function(data, response) {
				sys.puts(P['entry']);
				sys.puts(data);
		});
	});
}

http.createServer(function (request, response) {
	var data = '';
	
	request.addListener('body', function(chunk) {
		data += chunk;
	});
	
	request.addListener('complete', function() {
		var input = JSON.parse(data);
		
		for(i in input)
			processParams(
				crawlers[input[i]['crawler']],
				input[i]['security'],
				crawlers[input[i]['crawler']].actions['auth']('', input[i]['params'])
			);
	});
}).listen(SERVER_PORT);

sys.puts('Ready to serve, master!');
