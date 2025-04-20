### Requirements
There are two types of gateways that helps us in communicating with the web server
1. WSGI - Web Server Gateway Interface
2. ASGI = Asynchronous Server Gateway Interface

WSSI is synchronous which means that it can handle a single request at a time. MidAPI uses WSGI and we will use Gunicorn web server.

So, install Gunicorn using the command `pip install gunicorn`

To run the server, type the following command `gunicorn main:app`
Add `--reload` at the end to reload everything when a change has been made. `gunicorn main:app --reload`

Windows does not have 'fcntl' module that is required by gunicorn. So instead waitress wsgi can be used in its place.
To install waitress `pip install waitress`

To run the server, use the following command
`waitress-serve --host 127.0.0.1 main:midapi`