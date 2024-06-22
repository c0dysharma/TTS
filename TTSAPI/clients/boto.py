import boto3

from TTSAPI import settings

boto3.Session()
# Let's use Amazon S3


s3 = boto3.client('s3',
                  aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
                  aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY,
                  region_name=settings.AWS_SERVER_REGION)
