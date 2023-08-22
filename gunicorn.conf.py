workers = 2
worker_class = 'gevent'
bind = '0.0.0.0:5000'
accesslog = '-'
errorlog = '-'
reload = True
accesslog_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

