import boto3

# Resources
aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("techrescue")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
   
)

print(response)