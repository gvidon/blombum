#!/bin/bash

echo "[
	{'crawler': 'blogger', 'params': {
		'email'   : 'nenegoro@gmail.com',
		'password': 'zinaida123097',
		'blogid'  : '2590107552820081312',
		'body'    : 'пост ',
		'tags'    : 'тэг, еще, третий',
	}},

	{'crawler': 'blogger', 'params': {
		'email'   : 'nenegoro@gmail.com',
		'password': 'zinaida123097',
		'blogid'  : '1160797566605666733',
		'body'    : 'какой-то текст, тестатест',
		'tags'    : 'тэг, еще, третий',
	}}
]" | node worker.js
