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
		sudo('/etc/init.d/apache2 restart')
	
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
	run('cd '+REMOTE_PROJECT_ROOT+'; git pull origin master')

