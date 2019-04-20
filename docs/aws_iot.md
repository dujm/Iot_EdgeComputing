---
title: Connect to AWS IoT
---


####  [Project Page](https://dujm.github.io/Iot_EdgeComputing/index)&nbsp;  | &nbsp;   [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [AWS IoT Greengrass Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot_greengrass)&nbsp;  | &nbsp;   [AWS Machine Learning Interface](https://dujm.github.io/Iot_EdgeComputing/aws_ml)&nbsp;  | &nbsp;[GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)&nbsp;  | &nbsp; [Device: Camera Setup](https://dujm.github.io/Iot_EdgeComputing/device_cam)

<br>

#### 1. Prepare RPI  
```
# 1.1 Get the model of your RPI, RPI3B or B+ are  needed
cat /proc/cpuinfo

# 1.2 Determine the architecture of your RPI
uname -m
# The result must be greater than or equal to armv71

# 1.3 Set up RPI
https://docs.aws.amazon.com/greengrass/latest/developerguide/module1.html

# 1.4 Create a conda Python enviroment
conda create --name pinenuts python=3.6 -y

# 1.5 Activate environment
source activate pinenuts
```

<br>

### 2. Prepare using AWS IoT

```
# 2.1 Create an AWS account
https://aws.amazon.com/

# 2.2 Install git
sudo apt-get install git

# 2.3 Check OpenSSL version
python
>>> import ssl
>>> print(ssl.OPENSSL_VERSION)
OpenSSL 1.0.2r  26 Feb 2019
>>> exit()

# If the OpenSSL version is < 1.0.1, update OpenSSL for
your distribution
sudo apt-get update openssl
```

<br>

### 3. Connect to AWS IoT

### 3.1 Register a device
  * Choose Linux/OS
  * Choose Python
  * [Doc](https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/connectdevice/)

<br>

### 3.2 Download a connection kit
The connection kit includes some important components: security credentials, the SDK of your choice, and a sample project.
  * I downloaded the zip file to /home/pi/Iot_EdgeComputing/src

<br>

### 3.3 Configure and test your device
Using the connection kit, you will configure your device by transferring files and running a script, and test that it is connected to AWS IoT correctly.

```
# 1: Unzip the connection kit on the device
cd /home/pi/Documents/Iot_EdgeComputing/src
mkdir connect_device
unzip connect_device_package.zip -d connect_device

# 2: Add execution permissions
cd connect_device
chmod +x start.sh

# 3: Run the start script. Messages from your thing will appear below

./start.sh

# The aws-iot-device-sdk-python will automatically installed
# If ModuleNotFoundError: No module named 'AWSIoTPythonSDK'
pip install AWSIoTPythonSDK


# 4. Waiting for messages from your device
  '''
  Received a new message:
  {"message": "Hello World!", "sequence": 681}
  from topic:
  sdk/test/Python
  '''
```

<br>
