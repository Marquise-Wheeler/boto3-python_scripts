#!/usr/bin/env Python3

# This script adds a multiple items to the dynamodb table.

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

with table.batch_writer() as batch:
    batch.put_item(Item={"Name": "Marquise Wheeler01", "Email": "Test-Put_Item6641zgl@gmail.com"})
    batch.put_item(Item={"Name": "Marquise Wheeler02", "Email": "Test-Put_Item4322kdt@gmail.com"})
    batch.put_item(Item={"Name": "Marquise Wheeler03", "Email": "Test-Put_Item1651zny@gmail.com"})
    batch.put_item(Item={"Name": "Marquise Wheeler04", "Email": "Test-Put_Item322lzc@gmail.com"})
    batch.put_item(Item={"Name": "Marquise Wheeler05", "Email": "Test-Put_Item9487qns@gmail.com"})
    batch.put_item(Item={"Name": "Marquise Wheeler06", "Email": "Test-Put_Item1094bem@gmail.com"})
    batch.put_item(Item={"Name": "Marquise Wheeler07", "Email": "Test-Put_Item4481dps@gmail.com"})
    batch.put_item(Item={"Name": "Marquise Wheeler08", "Email": "Test-Put_Item7824qif@gmail.com"})
    batch.put_item(Item={"Name": "Marquise Wheeler09", "Email": "Test-Put_Item7481wzc@gmail.com"})
    batch.put_item(Item={"Name": "Marquise Wheeler10", "Email": "Test-Put_Item8661xrb@gmail.com"})
    
  