import boto3
from pprint import pprint
from uuid import uuid4
import time
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from werkzeug.security import generate_password_hash, check_password_hash

class UserController:

    def __init__(self, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
        self.table = dynamodb.Table('Users')

    def create(self, user):
        #create UUID
        # epoch = time.time()
        uniqueID = "%s" % (uuid4())
        print("User created with ID:", uniqueID)
        passwordHash = generate_password_hash(user['password'])

        
        try:
            response = self.table.put_item(
                Item={
                    'id': uniqueID,
                    'email': user['email'],
                    'password': passwordHash,
                    'firstName': user['firstName'],
                    'lastName': user['lastName']
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            response['userId'] = uniqueID
            response['email'] = user['email']
            response['firstName'] = user['firstName']
            response['lastName'] = user['lastName']
            return response


    def get(self, id):
        try:
            response = self.table.get_item(Key={'id': id})
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']

    def update(self, id, user):
        try:
            response = self.table.update_item(
                Key={
                    'id': id,
                },
                UpdateExpression="set email=:e, password=:p, firstName=:fn, lastName=:ln",
                ExpressionAttributeValues={
                    ':e': user['email'],
                    ':p': user['password'],
                    ':fn': user['firstName'],
                    ':ln': user['lastName']
                },
                ReturnValues="UPDATED_NEW"
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("updated user w/ id", id)
            return response

    def delete(self, id):
        try:
            response = self.table.delete_item(
                Key={
                    'id': id
                },
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("deleted user w/ id", id)
            return response
    

    def findUser(self, credentials):
        try:
            response = self.table.query(
                IndexName='email',
                KeyConditionExpression=Key('email').eq(credentials['email']),
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Items'][0]

    def verify_password(self, user, credentials):
        if not user or not check_password_hash(user['password'], credentials['password']):
            return False
        else:
            return True

    def authUser(self, credentials):
        user = self.findUser(credentials)
        auth = self.verify_password(user, credentials)
        if auth:
            del user["password"]
            return user
        else:
            return {"error": "email or password was incorrect"}

if __name__ == '__main__':
    controller = UserController()
    controller.create({
                    'id': "3",
                    'email': "meme@gmail.com",
                    'password': "pass",
                    'firstName': "first",
                    'lastName': "last"
                })
    user1 = controller.get("3")
    if user1:
        print('get user succeded')
        pprint(user1, sort_dicts=False)
    else:
        print('failed')
    user1['email'] = "change@gmail.com"
    controller.update("3", user1)
    changed1 = controller.get("3")
    print(changed1['email'])
    controller.delete("3")
