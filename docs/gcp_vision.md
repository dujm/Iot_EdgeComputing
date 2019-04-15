---
title: GCP Vision
---

####  [Project Page](https://dujm.github.io/Iot_EdgeComputing/index)&nbsp;  | &nbsp;   [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)



### 1. Set up Google Cloud Platform (GCP)
 * Go to [Create service account key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.262041677.-1312817518.1554382349&project=quiet-mechanic-236610&folder&organizationId)
  * Select project on top 'pines1'
  * Service account, my account 
  * JSON
 * Provide authentication credentials to your application code 
 * [Enable] billing(https://console.developers.google.com/billing/enable?project=650311275390) 

 ```
 export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/gcp/pines1-6e82e765805d.json"
 ``` 
 
 
### 2. Setup the client library on RPI
### Setting Up a Python Development Environment
[Doc](https://cloud.google.com/python/setup)
sudo apt update
sudo apt install python python-dev python3 python3-dev
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo pip install --upgrade virtualenv
# Successfully installed virtualenv-16.4.3

# Install google api 
[Doc](https://cloud.google.com/vision/docs/libraries#client-libraries-install-python)
cd Iot_EdgeComputing
virtualenv --python python3 env

source env/bin/activate
sudo env/bin/pip install google-cloud-storage
sudo env/bin/pip install google-cloud-vision
sudo env/bin/pip install google-api-python-client


# If you want to stop using the virtualenv and go back to your global Python, you can deactivate it:
#deactivate 


### 3. Test using a local image (cat)
 * [Download cat image](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/cloud-client/quickstart/resources/wakeupcat.jpg)
 
 * Write a python file /home/pi/Iot_EdgeComputing/gcp_vision.test.py

 * gcp_vision.test.py
 
 ```
 Labels:
Cat
Felidae
Whiskers
Facial expression
Small to medium-sized cats
Photo caption
Internet meme
European shorthair
Asian
Photography

 ```
### 4. Test using a local image (tree)
 * Write a python file /home/pi/Iot_EdgeComputing/gcp_vision.pines.py

 * gcp_vision.pines.py  
 
 ```
Labels:
Tree
shortleaf black spruce
Yellow fir
Columbian spruce
lodgepole pine
balsam fir
oregon pine
Tropical and subtropical coniferous forests
red pine
White pine
 ```
