var
	rest = require('./lib/restler'),
	sys  = require('sys');

var crawlers = {
	'blogger': require('./crawlers/blogger'),
};

// сделать запрос по параметрам текущего обработчика и отдать
// результаты для обработки следующему
function processParams(crawler, P) {
	rest.post(P['url'], {
		headers: P['HEADERS'],
		data   : P['POST'],
	}).addListener('complete', function(data, response) {
		P = crawler.actions[P['parser']](data, P);
		
		if(P['url']) {
			processParams(crawler, P);
			return false;
		}
		
		sys.puts(P['entry']);
	});
}

process.stdio.open();

//получить через stdin входные данные - массив с хэшами из:
//имени кроулера, ссылки (на которую отправить результат), параметрами и данными поста
process.stdio.addListener('data', function (data) {
	var input = JSON.parse(data);
	
	sys.puts(input[0]['crawler']);
	
	for(i in input)
		processParams(crawlers[input[i]['crawler']],
			crawlers[input[i]['crawler']].actions['auth']('', input[i]['params'])
		);
});
