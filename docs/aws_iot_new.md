---
title: Connect to AWS IoT
---


####  [Project Page](https://dujm.github.io/Iot_EdgeComputing/index)&nbsp;  | &nbsp;   [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)


### 1. Prepare RPI  
```
# Get the model of your RPI, RPI3B or B+ are  needed
cat /proc/cpuinfo

# Determine the architecture of your RPI
uname -m 
# The result must be greater than or equal to armv71 

# Set up RPI
https://docs.aws.amazon.com/greengrass/latest/developerguide/module1.html
```

```
# Create a conda Python enviroment
conda create --name pinenuts python=3.6 -y

# Activate environment
source activate pinenuts
```

<br>

### 2. Prepare using AWS IoT

```
# Create an AWS account
https://aws.amazon.com/

# Install git
sudo apt-get install git

# Check OpenSSL version
python
>>> import ssl
>>> print(ssl.OPENSSL_VERSION)
OpenSSL 1.0.2r  26 Feb 2019
>>> exit()
# If the OpenSSL version is < 1.0.1, update OpenSSL for
your distribution
sudo apt-get update openssl

```

### 3. Connect to AWS IoT
#### 3.1 Register a device
  * Choose Linux/OS
  * Choose Python
  * [Doc:Connect to AWS IoT](https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/connectdevice/)


#### 3.2 Download a connection kit
The connection kit includes some important components: security credentials, the SDK of your choice, and a sample project.
  * I downloaded the zip file to /home/pi/Iot_EdgeComputing/src


#### 3.3 Configure and test your device
Using the connection kit, you will configure your device by transferring files and running a script, and test that it is connected to AWS IoT correctly.

```
# Step 1: Unzip the connection kit on the device
cd /home/pi/Documents/Iot_EdgeComputing/src
mkdir connect_device
unzip connect_device_package.zip -d connect_device

# Step 2: Add execution permissions
cd connect_device
chmod +x start.sh

# Step 3: Run the start script. Messages from your thing will appear below

./start.sh

# The aws-iot-device-sdk-python will automatically installed
# If ModuleNotFoundError: No module named 'AWSIoTPythonSDK'
pip install AWSIoTPythonSDK
#or
# Install the AWS IoT Device SDK for Python:
cd /home/pi/Iot_EdgeComputing/src/connct_device
git clone https://github.com/aws/aws-iot-device-sdk-python.git
cd aws-iot-device-sdk-python
sudo python setup.py install



# Waiting for messages from your device
  '''
  Received a new message:
  {"message": "Hello World!", "sequence": 681}
  from topic:
  sdk/test/Python
  '''
```

### 4. Getting Started with AWS IoT Greengrass

#### 4. Module 1: Environment Setup for Greengrass  
[Doc](https://docs.aws.amazon.com/greengrass/latest/developerguide/module1.html)

```
# Check ip address
hostname -I

ssh pi@ip_address

sudo adduser --system ggc_user
sudo addgroup --system ggc_group

# Enable hardlink and softlink protection on the operating system at start up
cd /etc/sysctl.d
ls
vim 98-rpi.conf

'''
# Add 
fs.protected_hardlinks = 1
fs.protected_symlinks = 1
''' 

# Reboot the RPI
sudo reboot
```

```
ssh pi@192.168.178.29 
sudo sysctl -a 2> /dev/null | grep fs.protected

# Correct Output
'''
fs.protected_fifos = 0
fs.protected_hardlinks = 1
fs.protected_regular = 0
fs.protected_symlinks = 1

'''
```

```
# Enable and mount memory cgroups
cd /boot/
sudo vim cmdline.txt
# Append the below line, not as a newline
'''
cgroup_enable=memory cgroup_memory=1
'''

# Reboot the RPI
sudo reboot
```

```
# Run the Greengrass dependency checker
cd /home/pi/Iot_EdgeComputing/src/conda_env/conda_aws

# Download from aws-samples
# https://github.com/aws-samples/aws-greengrass-samples
wget https://github.com/aws-samples/aws-greengrass-samples/raw/master/greengrass-dependency-checker-GGCv1.8.0.zip

unzip greengrass-dependency-checker-GGCv1.8.x.zip

cd greengrass-dependency-checker-GGCv1.8.x
sudo modprobe configs
sudo ./check_ggc_dependencies | more

```

<br>

#### 4.2 Module 2: Installing the Greengrass Core Software
```
[Doc](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-device-start.html)
# 1. Sign in to the AWS Management Console
https://console.aws.amazon.com/

# 2. Choose IoT Greengrass
# Creat a group
# Name pinenuts
# Download the pipi_core resources as tar.gz to ./Iot_EdgeComputing/src/conda_env/conda_aws
# Download a root CA for AWS IoT
# Download the current Greengrass Core software
# https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html?icmpid=docs_gg_console#gg-core-download-tab
# For RPI: choose ARMv7l

# Copy downloaded files to root directory
cd Iot_EdgeComputing/src/conda_env/conda_aws 
sudo scp greengrass-linux-armv7l-1.8.1.tar.gz pi@192.168.178.29:/home/pi
sudo scp ab30d61810-setup.tar.gz pi@192.168.178.29:/home/pi

# Extract files
cd /home/pi

sudo tar -xzvf greengrass-linux-armv7l-1.8.1.tar.gz -C /
sudo tar -xzvf ab30d61810-setup.tar.gz -C /greengrass

# Use Amazon Trust Services (ATS) endpoints and ATS root CA certificates
cd /greengrass/certs/
sudo wget -O root.ca.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem

# Check the root.ca.pem file, if it's empty, re-run the above wget line 

# Start AWS IoT Greengrass on your core device
cd /greengrass/ggc/core/
sudo ./greengrassd start

# Correct output
'''
Setting up greengrass daemon
Validating hardlink/softlink protection
Waiting for up to 40s for Daemon to start

Greengrass successfully started with PID: 1130
'''
# Confirm that the AWS IoT Greengrass core software (daemon) is functioning
ps aux | grep 1130

```

#### 4.3 Module 3 (Part 1): Lambda Functions on AWS IoT Greengrass
[Doc](https://docs.aws.amazon.com/greengrass/latest/developerguide/module3-I.html)



--- 
### Errors
```
# Error: AWS Greengrass detected insecure OS configuration: No hardlink/softlink protection enabled.
cd /etc/sysctl.d
ls
vim 98-rpi.conf
```
