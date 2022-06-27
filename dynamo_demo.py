import boto3

#dynamodb = client.create_table("dynamodb")
dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Users',
	    KeySchema=[
			{
				'AttributeName': 'Name',
				'KeyType': 'HASH'
			}
			],
            AttributeDefinitions=[
			{
				'AttributeName': 'Name',
				'AttributeType': 'S'
			}
			],
            ProvisionedThroughput={
				'ReadCapacityUnits': 4,
				'WriteCapacityUnits': 4
            }
    )
	
print(table)