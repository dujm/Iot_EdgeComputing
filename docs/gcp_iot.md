---
title: Connect to Google IoT
---

####  [Project Page](https://dujm.github.io/Iot_EdgeComputing/index)&nbsp;  | &nbsp;   [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)


### 1. Preparing RPI



### 2. Setup

  * Log in
 ```
 gcloud auth login
 ```
  * Select project 'pines1'

### Enable Google Cloud IoT API
  * [Introduction](https://cloud.google.com/solutions/iot/?refresh=1)
  * Function: managing gateways and devices
  * [IoT API](https://console.cloud.google.com/?refresh=1&_ga=2.39660321.-364005320.1554372473)


### Enable Pub/Sub dashboard API
  * Function: real-time messaging, ingesting device telemetry
  * [Pub/Sub](https://console.cloud.google.com/cloudpubsub/enableApi?project=pines1&folder&organizationId)
  * Create a topic: nature
### 2. Register device
 Create a device registry[https://console.cloud.google.com/iot/registries?project=pines1]

  * Registry ID: pinenuts1
  * Region: europe-west1
  * Protocol: MQTT, HTTP

### 2. Allow IoT Core to send messages to Pub/Sub
 ```
 gcloud projects add-iam-policy-binding pines1 --member=serviceAccount:cloud-iot@system.gserviceaccount.com --role=roles/pubsub.publisher
 ```

 ---
 ### Reference
  * [Using Cloud IoT Core gateways with a Raspberry Pi](https://cloud.google.com/community/tutorials/cloud-iot-gateways-rpi)
  * [Google Cloud Doc](https://cloud.google.com/docs/?refresh=1)
  * [Overview of Internet of Things](https://cloud.google.com/solutions/iot-overview?refresh=1)
  * [Google Apps Script API](https://developers.google.com/apps-script/api/)
  * [Preparing Google Cloud IoT Core to Receive Messages](http://www.opensourcerers.org/connecting-iot-sensor-to-google-cloud-iot-core/)
  * [Raspberry Pi with Google IOT Core, PubSub, Cloud Functions and Firestore](https://my-bigdata-blog.blogspot.com/2019/02/raspberry-pi-with-google-iot-core-functions-firestore-bigquery.html)
  * Cloud IoT Edge, request need [AP alpha versionI](https://cloud.google.com/iot-edge/)


 ### Android of Things
  * [Raspberry Pi 3](https://developer.android.com/things/hardware/raspberrypi )
