---
title: How to setup the 
---


### 1. Setup the offical camera modules
```
sudo modprobe bcm2835-v4l2 
```

<br>

### 2.Set up a usb web cam
```
sudo apt-get install motion -y
lsusb
lsmod | grep uvc
sudo modprobe uvcvideo
v4l2-ctl --all
ls /dev/video*
v4l2-ctl -V


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

---
### References

 * [Raspberry Pi Camera and Motion out of the box – Sparrowcam](http://www.richardmudhar.com/blog/2015/02/raspberry-pi-camera-and-motion-out-of-the-box-sparrowcam/)
 * [How to setup a Raspberry Pi Camera](https://tutorials-raspberrypi.com/raspberry-pi-security-camera-livestream-setup/)
