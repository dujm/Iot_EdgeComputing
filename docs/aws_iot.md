
### Register a device#
A thing is the representation and record of your physical device in the cloud. Any physical device needs a thing record in order to work with AWS IoT.
  * Choose Linux/OS
  * Choose Python

### Download a connection kit
The connection kit includes some important components: security credentials, the SDK of your choice, and a sample project.

  * Download to a directory
  * Mine is /iot 



### Configure and test your device
Using the connection kit, you will configure your device by transferring files and running a script, and test that it is connected to AWS IoT correctly.

[Doc:Connect to AWS IoT](https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/connectdevice/)

[Doc:Install aws-iot-device-sdk-python](https://docs.aws.amazon.com/greengrass/latest/developerguide/IoT-SDK.html)

```
# Step 0 Setup 
# Install git 
sudo apt-get install git
# Install pdf reader
sudo apt-get install okular

# Install AWSIoTPythonSDK 
python
>>> import ssl
>>> print(ssl.OPENSSL_VERSION)
OpenSSL 1.1.0j  20 Nov 2018
>>> exit()

# install the AWS IoT Device SDK for Python:
cd iot 
git clone https://github.com/aws/aws-iot-device-sdk-python.git
cd aws-iot-device-sdk-python



```

```
# Step 1: Unzip the connection kit on the device
cd iot
mkdir connect_device
unzip connect_device_package.zip -d connect_device

# Step 2: Add execution permissions
cd connect_device
chmod +x start.sh

# Step 3: Run the start script. Messages from your thing will appear below

./start.sh

# Waiting for messages from your device

```
