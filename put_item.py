#!/usr/bin/env Python3

# This script adds a single item to the dynamodb table.

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')
response = table.put_item(
Item = {
    'Name': 'Marquise Wheeler',
    'Email': 'mardanmw27@gmail.com'
    }
)
print(response)
    
     