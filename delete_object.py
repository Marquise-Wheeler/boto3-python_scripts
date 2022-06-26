#!/usr/bin/env Python3

import boto3
import os
import glob

s3_resource=boto3.client("s3")


#s3_resource=boto3.client("s3")
# delete single object
#s3_resource.delete_object(Bucket='techrescue',
#    Key='Give-a-man-fish.png')

###################################    
# Find all bucket objects
objects=s3_resource.list_objects(Bucket="techrescue")["Contents"]
print("The total number of objects are:", len(objects))

# iteration
for object in objects:
    print(object["Key"])

###################################  
#delete multiple objects and print responses
for object in objects:
    response=s3_resource.delete_object(Bucket='techrescue',
      Key=object["Key"])
    print(response)
    
    