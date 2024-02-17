#!/usr/bin/env python3

import boto3
import os

BUCKET_NAME = 'sandbox-sample-202402'
S3_PATH_PREFIX = 'text/shakespeare'
s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET_NAME)

DIRECTORY = 'src'
for filename in os.listdir(DIRECTORY):
  full_path = os.path.join(DIRECTORY, filename)
  print('\nReading', full_path, '...')
  with open(full_path, 'r') as f:
    play = f.read()
    print('> Read', len(play), 'characters.')
    s3_full_path = os.path.join(S3_PATH_PREFIX, filename)
    bucket.put_object(Key=s3_full_path, Body=play)
    print('> Uploaded to S3 at', s3_full_path)

print('\nDone.')
