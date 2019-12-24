#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import web
import mysql.connector 
import json
from config import config 

conn = mysql.connector.connect(host=config['host'],user=config['user'], password=config['password'], database=config['database'])
cursor = conn.cursor()

class ImgBgList(object):
    def GET(self):
        # data=web.input()
        cursor.execute('select distinct(img_src),person_name from movie_person order by person_name limit 100')
        values = cursor.fetchall()
        list=[]
        for value in values:
            list.append(value[0])
        return json.dumps(list)
            
            
         