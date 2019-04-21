---
title: AWS SDK
---


####  [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [AWS IoT Greengrass Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot_greengrass)&nbsp;  | &nbsp;   [AWS Machine Learning Interface](https://dujm.github.io/Iot_EdgeComputing/aws_ml)

#### [AWS SDK Setup](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_cli)&nbsp;  | &nbsp; [AWS SDK Rekognition](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_reko)

#### [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)

#### [GCP SDK Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_sdk)

#### [Device: Camera Setup](https://dujm.github.io/Iot_EdgeComputing/device_cam)

<br>

### 1. Install AWS Command Line Interface (CLI)
[Doc](https://aws.amazon.com/cli/)

```
# Optional: activate conda environment
source activate pinenuts

# Install AWS CLI
pip install awscli

# Install command completion feature on Raspberry Pi’s CLI interface
complete -C aws_completer aws
```

<br>

### 2. Setup Security Credentials

[Security_credentials](
https://console.aws.amazon.com/iam/home?region=eu-west-1#/security_credentials) 

```
# 1) Create Access Key ID and secret access keys
'''
User on right top menu => 'My seceurity Credentials => Access keys => Create New Access Key => Download the csv to your local drive 
'''

# 2) In your local terminal 
aws configure

'''
AWS Access Key ID [None]: aaaaaaaaaaaaaa
AWS Secret Access Key [None]: aaaaaaaaaa
Default region name [None]: eu-west-1
Default output format [None]: json
'''
```

### 3. Use AWS SDK in your local terminal

```
# Create a new Thing 
aws iot create-thing --thing-name "YourThingName" 

#  List all your IoT Things
aws iot list-things

# List all your buckts
aws s3 ls 

# List the content in one bucket
aws s3 ls s3://greengrass-bucket-pinenuts

# Copy files to your bucket
aws s3 cp myfolder s3://greengrass-bucket-pinenuts --recursive
``` 


<br>

### 4. Use AWS SDK in Python (Boto3 package)

[Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)

```
# Install boto3
pip install boto3

# Use boto3
Python
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('test.jpg', 'rb')
s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)
```


