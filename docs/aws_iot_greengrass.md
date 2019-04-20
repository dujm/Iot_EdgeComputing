---
title: Connect to AWS IoT - Greegrass
---


####  [Project Page](https://dujm.github.io/Iot_EdgeComputing/index)&nbsp;  | &nbsp;   [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [AWS IoT Greengrass Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot_greengrass)&nbsp;  | &nbsp;   [AWS Machine Learning Interface](https://dujm.github.io/Iot_EdgeComputing/aws_ml)&nbsp;  | &nbsp;[GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)&nbsp;  | &nbsp; [Device: Camera Setup](https://dujm.github.io/Iot_EdgeComputing/device_cam)

<br>

#### Continue with [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)

### 4. Getting Started with AWS IoT Greengrass

### 4.1 Module 1: Environment Setup for Greengrass  
[Doc](https://docs.aws.amazon.com/greengrass/latest/developerguide/module1.html)

```
# 1. Check RPI ip address
hostname -I

ssh pi@ip_address

sudo adduser --system ggc_user
sudo addgroup --system ggc_group


# 2. Enable hardlink and softlink protection on the operating system at start up
cd /etc/sysctl.d
ls
vim 98-rpi.conf

'''
# Add two lines
fs.protected_hardlinks = 1
fs.protected_symlinks = 1
'''


# 3. Reboot the RPI
sudo reboot


# 4. Confirm harlink and softlink protection
ssh pi@192.168.178.29
sudo sysctl -a 2> /dev/null | grep fs.protected

# Correct Output
'''
fs.protected_fifos = 0
fs.protected_hardlinks = 1
fs.protected_regular = 0
fs.protected_symlinks = 1

'''


# 5. Enable and mount memory cgroups
cd /boot/
sudo vim cmdline.txt

# Append the below line, not as a newline
'''
cgroup_enable=memory cgroup_memory=1
'''

# Reboot the RPI
sudo reboot


# 6. Run the Greengrass dependency checker
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

### 4.2 Module 2: Installing the Greengrass Core Software
[Doc](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-device-start.html)

```
# 1. Sign in to the AWS Management Console
https://console.aws.amazon.com/


# 2. Create a IoT group
# Choose IoT Greengrass
# Creat a group
# Name pinenuts


# 3. Download the pipi_core resources as tar.gz to ./Iot_EdgeComputing/src/conda_env/conda_aws


# 4. Download the current Greengrass Core software
# https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html?icmpid=docs_gg_console#gg-core-download-tab
# For RPI: choose ARMv7l


# 5. Copy downloaded files to root directory
cd Iot_EdgeComputing/src/conda_env/conda_aws
sudo scp greengrass-linux-armv7l-1.8.1.tar.gz pi@192.168.178.29:/home/pi
sudo scp ab30d61810-setup.tar.gz pi@192.168.178.29:/home/pi


# 6. Extract files
cd /home/pi
sudo tar -xzvf greengrass-linux-armv7l-1.8.1.tar.gz -C /
sudo tar -xzvf ab30d61810-setup.tar.gz -C /greengrass


# 7. Use Amazon Trust Services (ATS) endpoints and ATS root CA certificates
cd /greengrass/certs/
sudo wget -O root.ca.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem

# Check the root.ca.pem file, if it's empty, re-run the above wget line


# 8. Start AWS IoT Greengrass on your core device
cd /greengrass/ggc/core/
sudo ./greengrassd start

# Correct output
'''
Setting up greengrass daemon
Validating hardlink/softlink protection
Waiting for up to 40s for Daemon to start

Greengrass successfully started with PID: 1130
'''


# 9. Confirm that the AWS IoT Greengrass core software (daemon) is functioning
ps aux | grep 1130
```

<br>

### 4.3 Module 3 (Part 1): Lambda Functions on AWS IoT Greengrass
[Doc](https://docs.aws.amazon.com/greengrass/latest/developerguide/module3-I.html)

```
# 1. Download AWS IoT Greegrass Core SDK
# Choose Python 2.7 v1.3 (Python 3 version is not available) https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html#gg-core-sdk-download


# 2. Decompress the downloaded SDK file
cd ~/Documents/Iot_EdgeComputing/src/conda_env
tar -xzvf greengrass-core-python-sdk-1.3.0.tar.gz -C conda_aws/


# 3. Create a Lambda function deployment package named hello_world_python_lambda.zip that contains greengrassHelloWorld.py and the greengrasssdk folder
# Install zip unzip
# sudo apt-get install zip unzip

# 1) Copy greengrassHelloWorld.py
cd aws_greengrass_core_sdk
scp examples/HelloWorld/greengrassHelloWorld.py sdk/

# 2) Uncompress greegrasssdk
cd sdk
unzip python_sdk_1_3_0.zip

# 3) zip
sudo zip -r hello_world_python_lambda.zip greengrasssdk greengrassHelloWorld.py


# 4) Create a Lambda function
# [Lambda](https://aws.amazon.com/lambda/)
# i) Create a function
'''
Author from scratch => Function name: Greegrass_HelloWorld => Runtime: Python 2.7 => Permissions/Chooseor create an execution role => Role name: Squirrel = Create function
'''

# ii) Upload your Lamda function deployment package
'''
Configuration Tab => Function code => Code entry type: Upload a zip file =>  Handler: greengrassHelloWorld.function_handler = Upload your zip file => Save
'''

# 5. Publish the Lamda function
'''
Dropdown Menu: Actions => Publish new version => Versiondescription: v1 => Publish
'''


# 6. Create an alias for the Lamda function
'''
Dropdown Menu: Actions => Create a new alias => Name: GG_HelloWorld => Version: 1
'''


# 7. Configure the Lambda function for AWS IoT Greegrass and test long-lived Lambda functions
'''
AWS IoT Core console, https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/dashboard

Choose Greengrass => Groups => Choose the group you created 'Pinenuts' => Choose Lambdas on the left menu => Add Lambda => Using existing Lambda 'GreenGrass_HelloWorld' => Select a Lambda version: Alias: GG_HelloWorld

Choose the ellipsis => Edit Configuration => Timeout: 25 Second =>Lamda Lifecycle: Make this function long-lived and keep it running indefinitely => Update
'''


# 8. Create a subscription that allows the Lambda to send MQTT messages to AWS IoT

'''
On the Group Configuration page https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/greengrass/groups/57f4f4b1-c66e-4201-a4c4-2c71c36d8251

Subscriptions => Add your first Subscription => Select a source: Lambdas tab: Greengrass_HelloWorld => Select a target: Service tab: IoT Cloud => Topic filter: hello/world => Next
'''


# 9. Deploy Cloud Configurations to an AWS IoT Greengrass Core Device
# 1) Make sure that the AWS IoT Greengrass daemon is running
ps aux | grep -E 'greengrass.*daemon'

# If the output doesn't contain a root entry for /greengrass/ggc/packages/1.8.1/bin/daemon, restart the daemon
cd /greengrass/ggc/core/
sudo ./greengrassd start

# 2) Deploy
# https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/greengrass/groups/57f4f4b1-c66e-4201-a4c4-2c71c36d8251
# Actions => Dploy => Automatic detection = Grant permission

# 3) Verify the Lambda function is running
'''
IoT console: https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/greengrass/grouphub

Test => Subscribe to topic => Subscription topic, enter hello/world => Quality of Service: choose 0 => MQTT payload display: choose Display payloads as strings

Publish messages:
Hello world! Sent from Greengrass Core running on platform: Linux-4.14.98-v7+-armv7l-with-debian-9.8
'''


# 10. Delete the function and subscription from the group
1 From the Lambdas page => choose the ellipsis (…) => Remove function

2) From the Subscriptions page => choose the ellipsis (…) => choose Delete

3) The function and subscription are removed from the core during the next group deployment
```
<br>

### 4.4 Module 3 (Part 2): Lambda Functions on AWS IoT Greengrass
 * [Doc](https://docs.aws.amazon.com/greengrass/latest/developerguide/package.html?shortFooter=true)  

```
# 1. Create and Package the Lambda Function similar to 4.3
cd  ~/Documents/Iot_EdgeComputing/src/conda_env/conda_aws/aws_greengrass_core_sdk/sdk/
wget https://raw.githubusercontent.com/aws-samples/aws-greengrass-samples/master/hello-world-counter-python/greengrassHelloWorldCounter.py

sudo zip -r hello_world_counter_python_lambda.zip greengrasssdk greengrassHelloWorldCounter.py

# 2. Test on-demand Lamda functions
```

<br>

---
### Errors
1. AWS Greengrass detected insecure OS configuration: No hardlink/softlink protection enabled.
 * Reason: Hardlink and softlink protection on the operating system at start up are not enabled

2. Can't import name.py file while creating a Lambda function
 * [Lambda Function](https://eu-central-1.console.aws.amazon.com/lambda/home?region=eu-central-1#/functions/Greengrass_HelloWorld_Counter?newFunction=true&tab=graph)
 * The name of name.py in the zip file should be the same as Handler info

3. Deployment failed

```
cd /greengrass/ggc/core/
sudo ./greengrassd stop
sudo ./greengrassd start
```



---  
### Terminology

#### What is a subscription?
A subscription consists of a source, target, and topic.
 * The source is the originator of the message.
 * The target is the destination of the message.
 * The topic allows you to filter the data that is sent from the source to the target.
 * The source or target can be a Greengrass device, Lambda function, connector, device shadow, or AWS IoT.
