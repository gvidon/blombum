var	sys		= require('sys'),
    base64	= require('../lib/vendor/base64');

exports.actions = {
	'auth': function(data, params) {
		return {
			'url': 'http://twitter.com/statuses/update.xml',

			'HEADERS': {
				'Authorization': 'Basic ' + base64.encode(params['login'] + ':' + params['password'])
			},

			'POST': {
				'status': params['status'],
			},

			'parser': 'grab'
		};
	},

	'grab': function(data, params) {
		return {'entry': data.status.id};
	}
};
