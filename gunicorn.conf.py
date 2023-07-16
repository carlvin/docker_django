workers = 2
syslog = True
bind = ['127.0.0.1:8000']
# Access log -records incoming HTTP requests
accesslog = "/var/log/gunicorn/accesslog.log"
#Error log - records gunicorn server goins-on
errorlog = "/var/log/gunicorn/error.log"
# Sending django output to the error log
capture_output = True
umask = 0
loglevel ="debug"
user = "xorb"
group = "xorb"

