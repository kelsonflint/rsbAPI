from decimal import Decimal
import json
import boto3

def load_users(users, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Users')
    for user in users:
        id = user['id']
        email = user['email']
        print("adding user:", id, email)
        table.put_item(Item=user)

def load_businesses(businesses, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
    
    table = dynamodb.Table('Businesses')
    for b in businesses:
        id = b['id']
        name = b['businessName']
        print("adding business:", id, name)
        table.put_item(Item=b)

def load_funding(fundingList, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Funding')
    for f in fundingList:
        id = f['id']
        name = f['fundingName']
        print("adding funding opportunity", id, name)
        table.put_item(Item=f)

def load_TA(taList, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('technicalAssistance')
    for ta in taList:
        id = ta['id']
        name = ta['orgName']
        print("adding ta:", id, name)
        table.put_item(Item=ta)
    
if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    with open("testUsers.json") as json_file:
        user_list = json.load(json_file, parse_float=Decimal)
    load_users(user_list, dynamodb)

    with open("testBusinesses.json") as json_file:
        business_list = json.load(json_file, parse_float=Decimal)
    load_businesses(business_list, dynamodb)

    with open("testFunding.json") as json_file:
        funding_list = json.load(json_file, parse_float=Decimal)
    load_funding(funding_list, dynamodb)

    with open("testTA.json") as json_file:
        ta_list = json.load(json_file, parse_float=Decimal)
    load_TA(ta_list, dynamodb)