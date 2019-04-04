---
title: Connect to AWS IoT
---


####  [Project Page](https://dujm.github.io/Iot_EdgeComputing/index)&nbsp;  | &nbsp;   [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)

### 1. Install aws-iot in Raspberry Pi
[Doc:Install aws-iot-device-sdk-python](https://docs.aws.amazon.com/greengrass/latest/developerguide/IoT-SDK.html)

```
# Install git
sudo apt-get install git

# Check OpenSSL version
python
>>> import ssl
>>> print(ssl.OPENSSL_VERSION)
OpenSSL 1.1.0j  20 Nov 2018
>>> exit()
# If the OpenSSL version is < 1.0.1, update OpenSSL for
your distribution
sudo apt-get update openssl

# Install the AWS IoT Device SDK for Python:
cd /home/pi/Iot_EdgeComputing/src
git clone https://github.com/aws/aws-iot-device-sdk-python.git
cd aws-iot-device-sdk-python
sudo python setup.py install

```
### 2. Connect to AWS IoT
#### 2.1 Register a device
  * Choose Linux/OS
  * Choose Python
  * [Doc:Connect to AWS IoT](https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/connectdevice/)


#### 2.2 Download a connection kit
The connection kit includes some important components: security credentials, the SDK of your choice, and a sample project.
  * I downloaded the zip file to /home/pi/Iot_EdgeComputing/src


#### 2.3 Configure and test your device
Using the connection kit, you will configure your device by transferring files and running a script, and test that it is connected to AWS IoT correctly.

```
# Step 1: Unzip the connection kit on the device
cd /home/pi/Iot_EdgeComputing/src
mkdir connect_device
unzip connect_device_package.zip -d connect_device

# Step 2: Add execution permissions
cd connect_device
chmod +x start.sh

# Step 3: Run the start script. Messages from your thing will appear below

./start.sh

# Waiting for messages from your device
  '''
  Received a new message:
  {"message": "Hello World!", "sequence": 681}
  from topic:
  sdk/test/Python
  '''
```

### 3. Setup AWS IoT Greengrass
AWS IoT Greengrass lets your devices process the data they generate locally, while still taking advantage of AWS services when an internet connection is available.  
[Doc](https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/greengrassIntro)
 * A series of clicks
   * Create a Group
   * Easy Group creation (recommended)
   * Name your Group: mine is 'PE'
   * Next  
   * Download tar.gz file



### 4. Get Started with Greengrass
[Jeff Barr's Blog](https://aws.amazon.com/blogs/aws/aws-greengrass-run-aws-lambda-functions-on-connected-devices/)
[Deploy local Lambda](bit.ly/greengrasstutorial)
