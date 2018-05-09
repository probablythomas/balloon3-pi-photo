#!/usr/bin/env python

import picamera
import time
import os

# AstroHackers Pi Camera launch
# instantiating PiCamera
print ('Starting camera recording')

rootpath = os.path.dirname(os.path.abspath(__file__))
mainpath = os.path.join(rootpath,'photos')

if not os.path.isdir(mainpath):
   os.mkdir(mainpath)

print ('Files save in "photos" subdirectory')

folder_count = len(next(os.walk(mainpath))[1])
output_path = os.path.join(mainpath,str(folder_count))

if not os.path.isdir(output_path):
   os.mkdir(output_path)


# photos will be captured in a sorta-never ending loop
for i in range(1,2000):
   with picamera.PiCamera() as camera:
      camera.resolution = (3280,2462)
      camera.start_preview()
      time.sleep(2)
      camera.capture(os.path.join(output_path,'pic%d.jpg' % i))
      print ('Captured pic%d.jpg' % i)

   time.sleep(15)

