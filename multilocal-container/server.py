#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 12:58:04 2018
@author: ahadmushir
@description: API module
"""

from flask import Flask, jsonify,render_template, Response
from flask import request
from flask import json
from flask import make_response, request, current_app
import redis

app = Flask(__name__)

#since we are using docker compose and with redis server container.
redis_host = "redis-server"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port,
                      password=redis_password, decode_responses=True)

@app.route('/alive', methods=['GET'])
def alive():
    message = jsonify({'prediction': 'About not to come'})
    

    
    msg = r.get("msg:hello")
    print(msg)
    return message


@app.route('/set', methods=['GET'])
def redis_set():
    r.set("msg:hello", "Hello Redis!!!")
    return jsonify({'Message': 'SET!'})


@app.route('/get', methods=['GET'])
def redis_get():
    msg = r.get("msg:hello")
    return jsonify({'Message': msg})



@app.route('/', methods=['GET'])
def root():
    return jsonify({'Message': 'This is a multi-local container api'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
