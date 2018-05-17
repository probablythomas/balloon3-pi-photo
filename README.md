# balloon3-pi-photo
Photography code for the third Astro Hackers balloon flight

Crontab
To make this run on boot, it is simplest to add a line to the crontab. The line will look similar to this:
@reboot python /home/pi/balloon3-pi-photo/pi-photo-v0.py

Dependencies
PiCamera in python
If you get an error when running this code, you don't have picamera installed. Run the installation by:
sudo apt install python-picamera python3-picamera
to install picamera for python 2.7 and python 3
