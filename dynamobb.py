import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table (
    TableName = 'Employees',
       KeySchema = [
           {
               'AttributeName': 'Name',
               'KeyType': 'HASH'
           },
           {
               'AttributeName': 'Email',
               'KeyType': 'RANGE'
           }
           ],
           AttributeDefinitions = [
               {
                   'AttributeName': 'Name',
                   'AttributeType': 'S'
               },
               {
                   'AttributeName':'Email',
                   'AttributeType': 'S'
               }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits':1,
                'WriteCapacityUnits':1
            }
          
    )
print(table)
    
# BASIC

# ADVANCED Use boto3 and Python to query a table, remove an item from a table, create a table, and delete a table.
# COMPLEX 
#1) Create a lambda function using boto3 and Python to query a table, return an item from a table and remove/delete an item from a table.
#2) Run a test of the lambda function to verify you were able to do all of the previous actions.
#3) Create APIs using API Gateway using the console that will each return query a table, return an item, delete an item by calling your lambda function.
#Note: You can reference the following documentation to point you in the right direction.
