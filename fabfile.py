import os
from datetime import datetime
from fabric   import *

REMOTE_HOST         = ''
REMOTE_PROJECT_ROOT = '/opt/webapps/dev/byteflow/'
GITHUB_REPO_URL     = 'git://github.com/gvidon/blombum.git'

#RESTART APACHE AFTER CODE UPDATE
def restart_apache(operation):
	def decorate():
		operation()
		sudo('/etc/init.d/apache2 stop')
		
		# to prevent cached settings.py bugs
		sudo('/etc/init.d/memcached restart')
		
		sudo('/etc/init.d/apache2 start')
	
	return decorate

#COMMIT CURRENT CODE TO DEV BRANCH(MASTER ON SERVER)
def commit():
	local('git pull origin master')
	local('git commit -am "auto commit by fabric"')
	local('git push origin master')

#COMMIT CURRENT CODE TO DEV BRANCH(MASTER ON SERVER)
@restart_apache
@hosts('174.143.147.61')
def deploy_dev():
	sudo('cd '+REMOTE_PROJECT_ROOT+'; git pull origin master')

#RESTART APACHE ON REMOTE HOST
@restart_apache
def restart_remote_apache():
	return 1

