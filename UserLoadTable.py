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
    
if __name__ == '__main__':
    with open("testUsers.json") as json_file:
        user_list = json.load(json_file, parse_float=Decimal)
    load_users(user_list)