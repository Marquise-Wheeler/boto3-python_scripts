#!/usr/bin/env Python3
# Search for S3 buckets using boto3
s3_buckets=[]
import boto3
resource=boto3.resource("s3")
resource.buckets.all()
for bucket in resource.buckets.all():
#    print(bucket) # will return s3.Bucket(name='NAME')
#    print(bucket.name) # Will return only the name
    s3_buckets.append(bucket) # Add bucket to list


print(s3_buckets) # print list


