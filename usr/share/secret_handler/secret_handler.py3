#!/usr/bin/env python3
import json
import boto3
import requests
import os
import argparse

parser = argparse.ArgumentParser(description='Get secret keys from AWS')

if os.environ.get('AWS_REGION') is not None:
  region = os.environ.get('AWS_REGION')
else:
  the_region = requests.get('http://169.254.169.254/latest/meta-data/placement/region')
  region = the_region.content

parser.add_argument('-r', '--region', default=region)

if os.environ.get('SECRET_ID') is not None:
  secret = os.environ.get('SECRET_ID')
else:
  secret = 'terminate-notice'

parser.add_argument('-i', '--id', default=secret)

key = os.environ.get('SECRET_KEY')
parser.add_argument('-k', '--key', default=key)

args = parser.parse_args()

if args.id is not None and args.key is not None:
  secrets_client = boto3.client('secretsmanager', region_name=args.region)
  secret_value = secrets_client.get_secret_value(SecretId=args.id)
  decoded_secret = json.loads(secret_value['SecretString'])
  print(decoded_secret[args.key])
else:
  print('')
