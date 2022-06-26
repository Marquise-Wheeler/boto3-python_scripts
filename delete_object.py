#!/usr/bin/env Python3

#import boto3


#s3_resource=boto3.client("s3")
# delete single object
#s3_resource.delete_object(Bucket='techrescue',
#    Key='Give-a-man-fish.png')

###################################    
#delete multiple objects
import boto3
import os
import glob

s3_resource=boto3.client("s3")
 
objects=s3_resource.list_objects(Bucket="techrescue")["Contents"]
print(len(objects))

###################################  