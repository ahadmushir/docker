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

app = Flask(__name__)


@app.route('/alive', methods=['GET'])
def alive():
    message = jsonify({'prediction': 'About not to come'})
    return message


@app.route('/', methods=['GET'])
def root():
    return jsonify({'Message': 'Sample REST Api'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
