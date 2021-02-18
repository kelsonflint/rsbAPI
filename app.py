import boto3
from flask import Flask, jsonify, request
from pprint import pprint
from businessController import BusinessController
from userController import UserController
from fundingController import FundingController
from taController import TAController
from decimal import Decimal

app = Flask(__name__)

#dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
user_controller = UserController(dynamodb)
business_controller = BusinessController(dynamodb)
funding_controller = FundingController(dynamodb)
ta_controller = TAController(dynamodb)

@app.route('/')
def index():
    return "this is the main page"

@app.route('/users', methods = ['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        json_request = request.get_json()
        response = user_controller.create(json_request)
        return jsonify(response)


@app.route('/users/<user_id>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def user(user_id=None):
    if request.method == 'GET':
        response = user_controller.get(user_id)
        return jsonify(response)
    
    if request.method == 'PUT':
        json_request = request.get_json()
        response = user_controller.update(user_id, json_request)
        return jsonify(response)

    if request.method == 'DELETE':
        response = user_controller.delete(user_id)
        return jsonify(response) 

@app.route('/users/<user_id>/businesses', methods = ['GET', 'POST'])
def userBusinesses(user_id=None):
    if request.method == 'GET':
        response = business_controller.get_user_businesses(user_id)
        for r in response:
            r = convert_decimal(r)
        pprint(response)
        return jsonify(response)
    if request.method == 'POST':
        json_request = request.get_json()
        response = business_controller.create(json_request)
        #add business to user list
        print(response)
        return jsonify(response)

@app.route('/users/<user_id>/businesses/<biz_id>', methods = ['GET', 'PUT', 'DELETE'])
def business(user_id=None, biz_id=None):
    if request.method == 'GET':
        response = convert_decimal(business_controller.get(user_id, biz_id))
        return jsonify(response)
    
    if request.method == 'PUT':
        json_request = request.get_json()
        response = business_controller.update(user_id, biz_id, json_request)
        return jsonify(response)

    if request.method == 'DELETE':
        response = business_controller.delete(user_id, id)
        return jsonify(response)

@app.route('/funding', methods = ['GET', 'POST'])
def allFunding():
    if request.method == 'GET':
        response = funding_controller.getAll()
        for r in response:
            r = convert_decimal(r)
        pprint(response)
        return jsonify(response)
    
    if request.method == 'POST':
        json_request = request.get_json()
        response = funding_controller.create(json_request)
        return jsonify(response)

@app.route('/funding/<id>', methods = ['GET', 'PUT', 'DELETE'])
def funding(id=None):
    if request.method == 'GET':
        response = funding_controller.get(id)
        pprint(response)
        return jsonify(response)
    
    if request.method == 'PUT':
        json_request = request.get_json()
        response = funding_controller.update(id, json_request)
        return jsonify(response)
    
    if request.method == 'DELETE':
        response = funding_controller.delete(id)
        return jsonify(response)

@app.route('/assistance', methods = ['GET', 'POST'])
def allAssistance():
    if request.method == 'GET':
        response = ta_controller.getAll()
        pprint(response)
        return jsonify(response)
    
    if request.method == 'POST':
        json_request = request.get_json()
        response = ta_controller.create(json_request)
        return jsonify(response)

@app.route('/assistance/<id>', methods = ['GET', 'PUT', 'DELETE'])
def assistance(id):
    if request.method == 'GET':
        response = ta_controller.get(id)
        pprint(response)
        return jsonify(response)
    
    if request.method == 'PUT':
        json_request = request.get_json()
        response = ta_controller.update(id, json_request)
        return jsonify(response)
    
    if request.method == 'DELETE':
        response = ta_controller.delete(id)
        return jsonify(response)



def convert_decimal(dictionary):
    """ Converts decimals to float and int. """

    for key in dictionary.keys():
        value = dictionary[key]
        if isinstance(value, Decimal):
            if value % 1 == 0:
                dictionary[key] = int(value)
            else:
                dictionary[key] = float(value)
        if isinstance(value, dict):
            value = convert_decimal(value)
                

    return dictionary

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

