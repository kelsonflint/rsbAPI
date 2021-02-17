import boto3
import time
from pprint import pprint
from uuid import uuid4
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

class BusinessController:

    def __init__(self, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
        self.table = dynamodb.Table('Businesses')

    def create(self, business):
        #create UUID

        try:
            response = self.table.put_item(Item=business)
        except ClientError as e:
           print(e.response['Error']['Message'])
        else:
            print('created new business', business['businessName'])
            return response

    def get(self, userId, id):
        try:
            response = self.table.get_item(
                Key={
                    'userId': userId,
                    'id': id
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']

    def get_user_businesses(self, userId):
        try:
            response = self.table.query(
                KeyConditionExpression=Key('userId').eq(userId)
            )
            print(response['Items'])
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Items']

    def update(self, userId, id, business):
        try:
            response = self.table.update_item(
                Key={
                    'id': id,
                    'userId': userId
                },
                UpdateExpression="set businessName=:n, address=:a, naics=:naics, numEmployees=:ne, timeInBusiness=:tib, annualRevenue=:ar, languagePref=:l, ownerDemographics=:od, reasonsForFunding=:rff, amountRequested=:amr, fundingTimeline=:ft, poc=:poc",
                ExpressionAttributeValues={
                    ':n': business['businessName'],
                    ':a': business['address'],
                    ':naics': business['naics'],
                    ':ne': business['numEmployees'],
                    ':tib': business['timeInBusiness'],
                    ':ar': business['annualRevenue'],
                    ':l': business['languagePref'],
                    ':od': business['ownerDemographics'],
                    ':rff': business['reasonsForFunding'],
                    ':amr': business['amountRequested'],
                    ':ft': business['fundingTimeline'],
                    ':poc': business['poc'],
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("updated business w/ id", id)
            return response
    
    def delete(self, userId, id):
        try:
            response = self.table.delete_item(
                Key={
                    'userId': userId,
                    'id': id
                },
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("deleted business w/ id", id)
            return response

if __name__ == '__main__':
    print('main')
    # controller = BusinessController()
    # biz = controller.get("1")
    # if biz:
    #     print('get biz succeeded')
    #     pprint(biz, sort_dicts=False)
    # else:
    #     print('get failed')
    # biz['businessName'] = 'memes'
    # controller.update("1", biz)
    # changed = controller.get("1")
    # print(changed['businessName'])
    # controller.delete("1")
    # controller.create(biz)
    # controller.get("1")
    # controller.delete("1")
