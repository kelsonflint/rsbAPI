import boto3
import time
from pprint import pprint
from uuid import uuid4
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

class FundingController:

    def __init__(self, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
        self.table = dynamodb.Table('Funding')

    def create(self, funding):
        try:
            response = self.table.put_item(Item=funding)
        except ClientError as e:
           print(e.response['Error']['Message'])
        else:
            print('created new funding', funding['fundingName'])
            return response

    def getAll(self):
        try:
            response = self.table.scan()['Items']
            pprint(response)
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response

    def get(self, id):
        try:
            response = self.table.get_item(
                Key={
                    'id': id
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']

    def update(self, id, f):
        try:
            response = self.table.update_item(
                Key={
                    'id': id
                },
                UpdateExpression="set fundingName=:fn, fundingType=:ft, provider=:p, website=:w, startDate=:sd, endDate=:ed, uses=:uses, description=:d, terms=:t, qualifications=:q",
                ExpressionAttributeValues={
                    ':fn': f['fundingName'],
                    ':ft': f['fundingType'],
                    ':p': f['provider'],
                    ':w': f['website'],
                    ':sd': f['startDate'],
                    ':ed': f['endDate'],
                    ':uses': f['uses'],
                    ':d': f['description'],
                    ':t': f['terms'],
                    ':q': f['qualifications']
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("updated funding w/ id", id)
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
            print("deleted funding w/ id", id)
            return response

if __name__ == '__main__':
    print('main')