import boto3
from pprint import pprint
from uuid import uuid4
import time
from botocore.exceptions import ClientError


class UserController:

    def __init__(self, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
        self.table = dynamodb.Table('Users')

    def create(self, id, email, password):
        #create UUID
        # epoch = time.time()
        # uniqueID = "%s_%d" % (uuid4, epoch)
        #hash password

        try:
            response = self.table.put_item(
                Item={
                    'id': id,
                    'email': email,
                    'password': password
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
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
    

if __name__ == '__main__':
    controller = UserController()
    controller.create("3", "me@gmail.com", "password")
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
