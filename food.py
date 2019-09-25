# -*- coding: utf-8 -*-

from ShortPackage.downloadVideo import downloadVideo
import os
from os import system
from dotenv import load_dotenv
load_dotenv()



if __name__ == '__main__':


    path = 'download'
    name = 'food-scientist'
    file_name = '%s/%s.mp4'%(path,name)

    srtPath =  os.getenv('VIDEO_SRT_PATH')

    url = 'https://video.epicurious.com/watch/4-levels-4-levels-of-steak-amateur-to-food-scientist'

    try:
        downloadVideo(url, file_name).run()

        srtName = '%s/%s.srt'%(path,name)

        p = system("autosub -S en -D en %s -o %s" % (file_name,srtName))

        system('mv %s %s'%(srtName,srtPath))
        system('rm -rf %s/*'%path)
        system('cd %s'%srtPath)
        system('git add .')
        system('git commit -a -m "%s"'%name)
        system('git push"')

    except Exception:
        print ("失败")