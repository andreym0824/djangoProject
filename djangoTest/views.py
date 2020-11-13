from typing import Dict, List, Any, Tuple

import os
from django.http import HttpResponse
import datetime
import requests
import json
from django.template.loader import get_template
import MySQLdb

def current_dateTime(request):
    now = datetime.datetime.now()
    t = get_template('html/dateTime.html')
    html = t.render({'current': {'time': now}})
    return HttpResponse(html)

def calcDateTime(request, month, day, model):
    now = "{}::{}--{}".format(datetime.datetime.now(), month, day)
    t = get_template('html/%s'%model+'.html')
    html = t.render({'current': {'time': now}})
    return HttpResponse(html)

def templateTest(request):
    jsonList = []
    req = requests.get('https://api.github.com/users/andreym0824')
    jsonList.append(json.loads(req.content.decode()))
    parsedData = {}
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
        userData['created_at'] = data['created_at']
        parsedData = {'name': userData['name'],
                  'created_at': userData['created_at'],
                  'public_repos': userData['public_repos'],
                  'email': userData['email']}
    t = get_template('html/profile.html')
    html = t.render({'users':parsedData})
    return HttpResponse(html)

def fetchMysql(request):
    db = MySQLdb.connect(user='root', db='wordpress_test', passwd='', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM `wp_users`')
    names = [row[1] for row in cursor.fetchall()]
    db.close()
    t = get_template('html/dbFetch.html')
    html = t.render({'names': names})
    return HttpResponse(html)