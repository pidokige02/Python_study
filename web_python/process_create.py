#!/usr/bin/python3

import cgi
form = cgi.FieldStorage()   # process_create.py s/w의 입력값을 저장하고 있다
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()

#Redirection
print("Location: index.py?id="+title)   # web browser 에게 web server가  이 location 으로 이동하라고 알려준다.
print()

