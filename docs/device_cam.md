---
title: Setup Raspberry Pi cameras
---


####  [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [AWS IoT Greengrass Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot_greengrass)&nbsp;  | &nbsp;   [AWS Machine Learning Interface](https://dujm.github.io/Iot_EdgeComputing/aws_ml)

#### [AWS SDK Setup](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_cli)&nbsp;  | &nbsp; [AWS SDK Rekognition](https://dujm.github.io/Iot_EdgeComputing/aws_sdk_reko)

#### [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)

#### [GCP SDK Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_sdk)

#### [Device: Camera Setup](https://dujm.github.io/Iot_EdgeComputing/device_cam)

<br>

### 1. Set up a RPI camera

```
# Install packages
pip3 install guizero
pip3 install twython
sudo apt-get install -y raspberrypi-ui-mods
sudo apt-get install -y raspberrypi-net-mods

# Take a photo
raspistill -o cam.jpg
```

<br>

### 3. Set up a usb web cam for taking photos

```
# 1) Install the fswebcam package
sudo apt-get install fswebcam

# 2) Add your user to video group
sudo usermod -a -G video pi

# 3) Basic usage to take a photo
fswebcam image.jpg

# 4) If you are using an old camera and get black imagaes, skip the first 20 frames
fswebcam -S 20 2image.jpg
```

<br> 

### 4. Set up a usb web cam for video streaming
```
# 1) Install the Motion tool
sudo apt-get install motion -y

# 2) Check if a usb camera can be detected
lsusb

# 3) Display all connected videodevices/cameras
ls /dev/video*
lsmod | grep uvc
sudo modprobe uvcvideo
sudo modprobe /dev/video0

v4l2-ctl --all

# 4) Check cameral details
v4l2-ctl -V

'''
Format Video Capture:
        Width/Height  : 640/480
        Pixel Format  : 'YUYV'
        Field         : None
        Bytes per Line: 1280
        Size Image    : 614400
        Colorspace    : SRGB
        Flags         :
'''

# 5) Edit Motion’s configuration file
sudo nano /etc/motion/motion.conf

# 6) Enable motion service
/etc/init.d/motion stop && fswebcam && /etc/init.d/motion start
'''
[....] Stopping motion (via systemctl): motion.service==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to stop 'motion.service'.
Multiple identities can be used for authentication:
 1.  ,,, (pi)
 2.  root
Choose identity to authenticate as (1-2): 1
Password: 
==== AUTHENTICATION COMPLETE ===
. ok 
--- Opening /dev/video0...
Trying source module v4l2...
/dev/video0 opened.
No input was specified, using the first.
Adjusting resolution from 384x288 to 352x288.
--- Capturing frame...
Captured frame in 0.00 seconds.
--- Processing captured image...
There are unsaved changes to the image.
[....] Starting motion (via systemctl): motion.service==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to start 'motion.service'.
Multiple identities can be used for authentication:
 1.  ,,, (pi)
 2.  root
Choose identity to authenticate as (1-2): 1
Password: 
==== AUTHENTICATION COMPLETE ===
. ok 

'''

# 7) Start motion service
sudo service motion start
sudo service motion stop
sudo service motion status

```
### 5. Install video player
```
# Note: mplayer and VLC player did not work well

# Install omxplayer
sudo apt-get install omxplayer
omxplayer /home/pi/Monitor/01-20190419104218.avi

# Key bindings
'''
 Increase Speed
2 Decrease Speed
j Previous Audio stream
k Next Audio stream
i Previous Chapter
o Next Chapter
n Previous Subtitle stream
m Next Subtitle stream
s Toggle subtitles
q Exit
Space or p Pause/Resume
– Decrease Volume
+ Increase Volume
Left Seek -30
Right Seek +30
Down Seek -600
Up Seek +600
'''
```

---
### References
 * [Using a standard USB webcam](https://www.raspberrypi.org/documentation/usage/webcams/)
 * [Motion](https://motion-project.github.io/motion_guide.html)
 * [omxplayer](https://raspberry-projects.com/pi/software_utilities/media-players/omxplayer)
 * [Raspberry Pi Camera and Motion out of the box – Sparrowcam](http://www.richardmudhar.com/blog/2015/02/raspberry-pi-camera-and-motion-out-of-the-box-sparrowcam/)
 * [How to setup a Raspberry Pi Camera](https://tutorials-raspberrypi.com/raspberry-pi-security-camera-livestream-setup/)
