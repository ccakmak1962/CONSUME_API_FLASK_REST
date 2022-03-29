from flask import request, jsonify
import json
import requests
from requests.exceptions import HTTPError

# get all courses   
api_url = "http://localhost:3500/courses"
response = requests.get(api_url)
for d in response.json():
    # use get for safety
    print( str(d.get('course_id')) + ' - \t' + d.get('course_name') + '\t\t -  ' + d.get('course_topic'))
    
#get specific course
## api_url = "http://localhost:3500/courses/9"
## response = requests.get(api_url)
## print(response.json())

# insert new course
## api_url = "http://localhost:3500/courses"
## todo = {"course_name": "SQL/DS", "course_topic": "SQL-DS Learn"}
## response = requests.post(api_url, json=todo)
## print(response. json())