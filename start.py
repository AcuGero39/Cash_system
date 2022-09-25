import socket
import sys
import os


sys.exit(
	os.system(
		f'python manage.py runserver {socket.gethostbyname(socket.getfqdn())}:80'
	)
)