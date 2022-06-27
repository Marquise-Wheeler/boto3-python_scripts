#!/usr/bin/env Python3

# This script adds a multiple items to the dynamodb table.

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')
response = table.scan()
#print(response,"\n")
#print(len(response))
response['Items']
print(len(response),"\n")
print(response)
    