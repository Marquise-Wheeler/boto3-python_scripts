#!/usr/bin/env Python3

import boto3
import os
import glob

s3_resource=boto3.client("s3")

# Find all bucket objects
objects=s3_resource.list_objects(Bucket="techrescue")["Contents"]
print("The total number of objects are:", len(objects))

# iteration
for object in objects:
    print(object["Key"])