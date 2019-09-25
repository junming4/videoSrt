#!/bin/bash

cd /home/www/var/videoSrt
echo `pwd`
git add .
git commit -a -m "system"
git push
