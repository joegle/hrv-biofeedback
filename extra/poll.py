# Copyright (c) 2014 Joseph Wright <joegle@gmail.com>
# License: BSD 3 clause

import cgi
import redis
#import cgitb; cgitb.enable()

form = cgi.FieldStorage()

if "key" not in form:
    resp="key param must be supplied: poll.py?key=u10"
    print "Status: 400"
else:
    key = str(form.getvalue('key'))
    redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0)
    resp = redis_conn.get(key)
    if resp is None:
        resp="'%s' is not valid key, use u10, u50, or u100"%key
        print "Status: 400"

print "Content-Type: text/plain"
print 
print resp

