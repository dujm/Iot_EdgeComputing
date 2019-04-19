---
title: How to setup a Raspberry Pi camera
---


####  [Project Page](https://dujm.github.io/Iot_EdgeComputing/index)&nbsp;  | &nbsp;   [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)&nbsp;  | &nbsp; [Device: Camera Setup](https://dujm.github.io/Iot_EdgeComputing/device_cam)


### 1. Set up a usb web cam for taking photos

```
# Install the fswebcam package
sudo apt-get install 

#Add your user to video group
sudo usermod -a -G video pi

# Basic usage to take a photo
fswebcam image.jpg

# If you are using an old camera and get black imagaes, skip the first 20 frames
fswebcam -S 20 2image.jpg
```

<br> 

### 2.Set up a usb web cam for video streaming
```
# Install the Motion tool
sudo apt-get install motion -y

# Check if a usb camera can be detected
lsusb

# Display all connected videodevices/cameras
ls /dev/video*
lsmod | grep uvc
sudo modprobe uvcvideo
sudo modprobe /dev/video0

v4l2-ctl --all

# Check cameral details
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
```
```
# Edit Motion’s configuration file
sudo nano /etc/motion/motion.conf
```


```

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
```

```
# Start motion service
sudo service motion start
sudo service motion stop
sudo service motion status

```
### 3. Install video player
```
# 
# mplayer and VLC player did not work well

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
