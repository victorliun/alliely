from fabric.api import * 

env.hosts = ['123.456.78.90:1234'] 
env.user = "root"

def update_django_project():      
	""" Updates the remote django project."""     
 	with cd('/home/****/www/****/******'):          
		run('git pull origin master')  	
	with prefix('source ../bin/activate'):  	    
		run('pip install -r requirements.txt')  	   
		run('python manage.py syncdb')          
		# run('python manage.py schemamigration **** --auto')          
		run('python manage.py migrate ****')          
		run('python manage.py collectstatic --noinput')
 
def restart_webserver():      
	""" Restarts remote nginx and uwsgi"""     
	sudo("killall -s HUP /home/****/www/****/bin/uwsgi")      
	sudo("nginx -s stop")
	sudo("/etc/rc.d/nginx start ")


 
def deploy():
    """ Deploy Django Project."""      

	update_django_project()      
	restart_webserver() 

