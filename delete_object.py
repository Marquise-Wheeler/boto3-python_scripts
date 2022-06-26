#!/usr/bin/env Python3

import boto3

s3_resource=boto3.client("s3")
s3_resource.delete_object(Bucket='techrescue',
    Key='Give-a-man-fish.png')