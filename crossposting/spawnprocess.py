#!/usr/bin/python

import subprocess

subprocess.Popen([
	'/home/nide/code/kanobu/src/manage.py', 'rebuildindex', '--site_id', '4', '--parse', 'none'
])

subprocess.Popen([
	'node', '/home/nide/code/blombum/crossposting/test.js'
], stdin = subprocess.PIPE).communicate('[{somevar: 1}, {somevar: 44}, {somevar: 22}]')

print 'kuku'
