---
title: Connect to Google IoT
---


####  [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [AWS IoT Greengrass Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot_greengrass)&nbsp;  | &nbsp;   [AWS Machine Learning Interface](https://dujm.github.io/Iot_EdgeComputing/aws_ml)

#### [AWS SDK Setup](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_cli)&nbsp;  | &nbsp; [AWS SDK Rekognition](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_reko)

#### [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)

#### [GCP SDK Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_sdk)

#### [Device: Camera Setup](https://dujm.github.io/Iot_EdgeComputing/device_cam)

<br>

### 1. Set Up a conda Python environment in RPI  

```
cd Iot_EdgeComputing/conda_env 
conda env create -f pineapple.yml

# Activate environment
source activate pineapple
```

<br>

### 2. Setup GCloud IoT Core
### 2.1 GCloud setup

```
# Log in 
gcloud auth login

# Update GCloud components
gcloud components update

# Create and set a new project 
gcloud projects create pineapples

# Set to the new project
gcloud config set project pineapples
 ```
 
 <br>
   
### 2.2 Enable Billing
 * [Go to Project List Page](https://console.developers.google.com/cloud-resource-manager?previousPage=%2Fbilling%2Fenable%3Fproject%3Dpines1%26pli%3D1)
 * Select Project and click the 'Three dots' on the right  => Billing => Link to your billing account  
 
 <br>
  
### 2.3 Enable Google Cloud IoT API
  * [Cloud IoT Core](https://cloud.google.com/iot-core/?refresh=1)
  * [Click 'View Console'] (https://console.cloud.google.com/iot?refresh=1&_ga=2.104796928.-1458619743.1555602826)
  * Enable API 
  * Function: managing gateways and devices

<br>
   
### 2.4 Enable Pub/Sub dashboard API
  * [Pub/Sub](https://console.cloud.google.com/cloudpubsub/enableApi?project=pineapples&folder&organizationId)
  * Create a topic: iot 
  * Function: real-time messaging, ingesting device telemetry 
  
 <br>

### 2.5 Allow IoT Core to send messages to Pub/Sub
 ```
 gcloud projects add-iam-policy-binding pineapples --member=serviceAccount:cloud-iot@system.gserviceaccount.com --role=roles/pubsub.publisher
 ```

 <br>
   
### 3. Register a device
### 3.1 Create a device registry
  * [Registry](https://console.cloud.google.com/iot/registries?project=pineapples)
  * Registry ID: pineapple1
  * Region: europe-west1
  * Protocol: MQTT, HTTP
  * Cloud Pub/Sub Topic: projects/pineapples/topics/iot
  
 <br>

### 3.2 Set up the RPI as a device
```
cd Iot_EdgeComputing/src
# Clone the GCP community repo
git clone https://github.com/GoogleCloudPlatform/community.git

# Install Python dependencies
sudo rm -r community/.git
cd community/tutorials/cloud-iot-gateways-rpi
pip install -r requirements-pi.txt 

# Export environment dependencies to yml
conda env export > ~/Documents/Iot_EdgeComputing/conda_env/pineapples_iot_rpi_device.yml


```
---
### References
  * [Using Cloud IoT Core gateways with a Raspberry Pi](https://cloud.google.com/community/tutorials/cloud-iot-gateways-rpi)
  * [Google Cloud Doc](https://cloud.google.com/docs/?refresh=1)
  * [Overview of Internet of Things](https://cloud.google.com/solutions/iot-overview?refresh=1)
  * [Google Apps Script API](https://developers.google.com/apps-script/api/)
  * [Preparing Google Cloud IoT Core to Receive Messages](http://www.opensourcerers.org/connecting-iot-sensor-to-google-cloud-iot-core/)
  * [Raspberry Pi with Google IOT Core, PubSub, Cloud Functions and Firestore](https://my-bigdata-blog.blogspot.com/2019/02/raspberry-pi-with-google-iot-core-functions-firestore-bigquery.html)
  * [Cloud IoT Edge alpha versionI](https://cloud.google.com/iot-edge/)
  * [Android of Things](https://developer.android.com/things/hardware/raspberrypi )
