# predict_s3_pines.py

import os, json,time
import boto3
from pandas.io.json import json_normalize
os.chdir('images')
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
img_name = str(data.name)+ '_s3_' + time.strftime('%Y%m%d-%H%M%S') + '_'+ 'reko_prediction.json'

with open(img_name, 'w') as outfile: 
	json.dump(response, outfile)

# Write results to a csv file with current date and time
csv_name = str(data.name)+ '_s3_' + time.strftime('%Y%m%d-%H%M%S') + '_'+ 'reko_prediction.csv'

df = json_normalize(response['Labels'])
df.to_csv(csv_name)

# Pretty print to terminal	
response_json = json.dumps(response, indent=4)
print('The image is',data.name)
print(response_json)

os.chdir('..')
