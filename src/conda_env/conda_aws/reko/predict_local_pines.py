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

# Get an image from local file ============> Change to your file
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
json_name = str(img_name)+ '_local_'  + time.strftime('%Y%m%d-%H%M%S') + '_'+ 'reko_prediction.json'
with open(json_name, 'w') as outfile: 
	json.dump(response, outfile)

# Write results to a csv file with current date and time
csv_name = str(img_name)+ '_local_' + time.strftime('%Y%m%d-%H%M%S') + '_'+ 'reko_prediction.csv'

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
