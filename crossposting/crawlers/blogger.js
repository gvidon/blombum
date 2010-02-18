var sys = require('sys'), libxml = require('../lib/libxmljs');

exports.actions = {
	'auth': function(data, params) {return {
		'url'   : 'https://www.google.com/accounts/ClientLogin',
		'parser': 'post',
		'blogid': params['blogid'],
		
		'body'  : params['body'],
		'tags'  : params['tags'],
		
		'HEADERS': {},
		
		'POST': {
			'Email'      : params['email'],
			'Passwd'     : params['password'],
			'service'    : 'blogger',
			'accountType': 'GOOGLE',
			'source'     : 'blombum-worker-1',
		},
	}},
	
	'post': function(data, params) { return {
		'url'   : 'http://www.blogger.com/feeds/'+params['blogid']+'/posts/default',
		'parser': 'grab-post-url',
		
		'HEADERS': {
			'Authorization': 'GoogleLogin auth='+RegExp('Auth=(.*)\n')(data)[1],
			'Content-type' : 'application/atom+xml',
		},
		
		'POST': '<entry xmlns="http://www.w3.org/2005/Atom">\
				<title type="text">test</title>\
				\
				<content type="xhtml"><div xmlns="http://www.w3.org/1999/xhtml">\
						'+params['body']+'\
				</div></content>\
				\
				<category scheme="http://www.blogger.com/atom/ns#" term="marriage" />\
				<category scheme="http://www.blogger.com/atom/ns#" term="Mr. Darcy" />\
			</entry>',
	}},
	
	'grab-post-url': function(data, params) {
		return {'entry': libxml.parseHtmlString(data).get('//entry/link[@rel="alternate"]/@href').children()[0].text()};
	},
};
