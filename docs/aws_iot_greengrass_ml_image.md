---
title: AWS IoT Greengrass Image Classification Connector
---


####  [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [AWS IoT Greengrass Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot_greengrass)&nbsp;  | &nbsp;   [AWS Machine Learning Interface](https://dujm.github.io/Iot_EdgeComputing/aws_ml)

#### [AWS SDK Setup](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_cli)&nbsp;  | &nbsp; [AWS SDK Rekognition](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_reko)

#### [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)

#### [GCP SDK Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_sdk)

#### [Device: Camera Setup](https://dujm.github.io/Iot_EdgeComputing/device_cam)

<br>

###  0. Prerequisites
 * Hardware:
   * Raspberry Pi 3 Model B
   * Raspberry Pi Camera Module V2 – 8 Megapixel, 1080p
 * Software:
   * A Greengrass group deployed to your Raspberry Pi that is running AWS IoT Greengrass Core v1.7.0.
   * Your Greengrass group has an IAM group role, at minimum:  
    * the AWSGreengrassResourceAccessRolePolicy  
    * AWSGreengrassFullAccess policies attached
  * [Doc](https://docs.aws.amazon.com/greengrass/latest/developerguide/ml-dlc-console.html)

<br>

### 1. Install the dependencies for the Apache MXNet framework

```
# Temporarily increase the swap size for installing scipi
sudo vim /etc/dphys-swapfile
# Change CONF_SWAPSIZE = 1000
/etc/init.d/dphys-swapfile restart

# Activate environment
source activate pinenuts

# Save the file armv7l.sh
cd Iot_EdgeComputing/src/conda_env/conda_aws/aws_greegrass_image_connector
sudo bash armv71.sh
```

<br>


### 2. Install the Apache MXNet Framework
[
Download ggc-mxnet-v1.2.1-python-raspi.tar.gz](https://greengrass-machine-learning-pdx.s3.us-west-2.amazonaws.com/mxnet/ggc-mxnet-v1.2.1-python-raspi.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20190420T184724Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=AKIA3LRYJL3ITQX3ZWKI%2F20190420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=e88b051929444b0c72d11d34d5bafe6d25784a29d54c53d5255fe216c133be3d)
```
# Install the MXNet framework
scp ggc-mxnet-v1.2.1-python-raspi.tar.gz pi@192.168.178.29:/home/pi

# Install the MXNet framework
cd /home/pi
tar -xzf ggc-mxnet-v1.2.1-python-raspi.tar.gz
cd ggc-mxnet-v1.2.1-python-raspi
./mxnet_installer.sh

# Copy file to my project repo
scp greengrassObjectClassification.zip ~/Documents/Iot_EdgeComputing/src/conda_env/conda_aws/ml_interface

```

<br>

### 3. Install Image Classification connector


---
### Errors
1. Unmet dependencies  

```
sudo apt --fix-broken install
```
