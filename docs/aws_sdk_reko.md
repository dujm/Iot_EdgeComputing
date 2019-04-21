---
title: AWS SDK Rekognition
---


####  [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [AWS IoT Greengrass Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot_greengrass)&nbsp;  | &nbsp;   [AWS Machine Learning Interface](https://dujm.github.io/Iot_EdgeComputing/aws_ml)

#### [AWS SDK Setup](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_cli)&nbsp;  | &nbsp; [AWS SDK Rekognition](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_reko)

#### [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)

#### [GCP SDK Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_sdk)

#### [Device: Camera Setup](https://dujm.github.io/Iot_EdgeComputing/device_cam)

<br>

### 0 Prerequisite
 * Step 1: Set Up an AWS Account and Create an IAM User
 * Step 2: Set Up the AWS CLI and AWS SDKs
 * [AWS Doc](https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html)
 * [My Doc](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_cli)



### 1. Image recognition using AWS CLI

```
# 1. Example in the tutorial:
aws rekognition detect-labels --image "S3Object={Bucket=console-sample-images-dub,Name=skateboard.jpg}" --region eu-west-1

# 2. Use our image of pines 
# Copy files to your bucket
aws s3 cp /home/pi/Documents/Iot_EdgeComputing/src/images s3://pinenutswest --recursive

aws rekognition detect-labels \
  --image "{\"S3Object\":{\"Bucket\":\"pinenutswest\",\"Name\":\"pines.jpeg\"}}" \
  --region eu-west-1 \
  > prediction.json
```

```
# Result  
'''
{
    "Labels": [
        {
            "Name": "Plant",
            "Confidence": 99.9062271118164,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Tree",
            "Confidence": 99.9062271118164,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Plant"
                }
            ]
        },
        {
            "Name": "Pine",
            "Confidence": 99.32074737548828,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Plant"
                },
                {
                    "Name": "Tree"
                }
            ]
        },
        {
            "Name": "Conifer",
            "Confidence": 97.8804931640625,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Plant"
                },
                {
                    "Name": "Tree"
                }
            ]
        },
        {
            "Name": "Art",
            "Confidence": 75.68220520019531,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Painting",
            "Confidence": 75.68220520019531,
            "Instances": [
                {
                    "BoundingBox": {
                        "Width": 0.9723396301269531,
                        "Height": 0.8938464522361755,
                        "Left": 0.015554961748421192,
                        "Top": 0.10115352272987366
                    },
                    "Confidence": 75.68220520019531
                }
            ],
            "Parents": [
                {
                    "Name": "Art"
                }
            ]
        },
        {
            "Name": "Abies",
            "Confidence": 68.67780303955078,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Plant"
                },
                {
                    "Name": "Tree"
                }
            ]
        },
        {
            "Name": "Fir",
            "Confidence": 68.67780303955078,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Plant"
                },
                {
                    "Name": "Tree"
                }
            ]
        },
        {
            "Name": "Larch",
            "Confidence": 65.95524597167969,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Plant"
                },
                {
                    "Name": "Tree"
                },
                {
                    "Name": "Conifer"
                }
            ]
        }
    ],
    "LabelModelVersion": "2.0"
}
'''  
```

<br>

### 2. Reko Image recognition 

### 2.1 An image uploaded to S3
```
# predict_s3_pines.py
import os, time
import json
import boto3

os.chdir('/home/pi/Documents/Iot_EdgeComputing/src/conda_env/conda_aws/reko/images')
# Connect to Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
#for bucket in s3.buckets.all():
    #print(bucket.name)

# Upload a new file to S3
data = open('pines.jpeg', 'rb')
s3.Bucket('pinenutswest').put_object(Key='pines.jpeg', Body=data)

# Connect to Reko API
client = boto3.client('rekognition', region_name='eu-west-1')

# Object for prediction
response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'pinenutswest',
            'Name': 'pines.jpeg'
        }
    },
    MaxLabels=123,
    MinConfidence= 90
)
# Write to a json file with current date and time
file_name = str(data.name)+ '_' + time.strftime('%Y%m%d-%H%M%S') + '_'+ 'reko_prediction.json'

with open(file_name, 'w') as outfile: 
	json.dump(response, outfile)
	
# Pretty print to terminal	
response_json = json.dumps(response, indent=4)
print('The image is',data.name)
print(response_json)
```

```
# Result
'''
{
    "Labels": [
        {
            "Name": "Tree",
            "Confidence": 99.9062271118164,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Plant"
                }
            ]
        },
        {
            "Name": "Plant",
            "Confidence": 99.9062271118164,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Pine",
            "Confidence": 99.32074737548828,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Tree"
                },
                {
                    "Name": "Plant"
                }
            ]
        },
        {
            "Name": "Conifer",
            "Confidence": 97.8804931640625,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Tree"
                },
                {
                    "Name": "Plant"
                }
            ]
        }
    ],
    "LabelModelVersion": "2.0",
    "ResponseMetadata": {
        "RequestId": "9354619e-6451-11e9-8804-af6b83ef2c35",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "content-type": "application/x-amz-json-1.1",
            "date": "Sun, 21 Apr 2019 16:21:54 GMT",
            "x-amzn-requestid": "9354619e-6451-11e9-8804-af6b83ef2c35",
            "content-length": "419",
            "connection": "keep-alive"
        },
        "RetryAttempts": 0
    }
}

'''
```

<br>

### 2.2 An image on local storage
```
# predict_local_pines.py
import os, json,time
import boto3

from pandas.io.json import json_normalize

# Functions
def get_image(image):
	'''
	image is the the image file name
	'''
	with open (image, 'rb') as imgfile:
		return imgfile.read(),str(image)
		
# Change directory to images/
os.chdir('images')

# Get an image from local file
imgb, img_name = get_image(r'pines.jpeg')

# Connect to Reko API
client = boto3.client('rekognition', region_name='eu-west-1')

# Object for prediction
response = client.detect_labels(
    Image={
		'Bytes': imgb
        },
    MaxLabels=123,
    MinConfidence= 90
)
# Write results to a json file with current date and time
json_name = str(img_name)+ '_' + time.strftime('%Y%m%d-%H%M%S') + '_'+ 'reko_prediction.json'
with open(json_name, 'w') as outfile: 
	json.dump(response, outfile)

# Write results to a csv file with current date and time
csv_name = str(img_name)+ '_' + time.strftime('%Y%m%d-%H%M%S') + '_'+ 'reko_prediction.csv'

df = json_normalize(response['Labels'])
df.to_csv(csv_name)

# Print information to terminal
# Print image name	
print('The image is',img_name)


# Print predicted results
response_json = json.dumps(response, indent=4)
print(response_json)

# Change back to the upper level of directory
os.chdir('..')
```
<br>

---
### References
 * [Amazon Rekognition using Python (boto3)](https://medium.com/@ankiijindal/amazon-rekognition-using-python-boto3-23982ba8fda7)

<br>

---
### Errors

1. Could not connect to the endpoint URL: "https://rekognition.eu-central-1.amazonaws.com/"
 * region name is not specified
 * client = boto3.client('rekognition', region_name='eu-west-1')

<br>

---
### Installation of packages used  in this tutorial
```
python -mpip install matplotlib
conda install pandas
pip install image
conda install -y -c conda-forge opencv
```
