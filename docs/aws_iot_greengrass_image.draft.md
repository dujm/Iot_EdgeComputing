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
  * [Getting Started with AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-gs.html)

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

### 2. Install Image Classification connector


---
### Errors
1. Unmet dependencies
```
sudo apt --fix-broken install
```
