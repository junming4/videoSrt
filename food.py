# -*- coding: utf-8 -*-

from ShortPackage.downloadVideo import downloadVideo
import os
from os import system
from dotenv import load_dotenv
load_dotenv()



if __name__ == '__main__':


    name = 'over-easy-egg'

    file_name = '%s.mp4'%name

    srtPath =  os.getenv('VIDEO_SRT_PATH')

    url = 'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-make-an-over-easy-egg'

    try:
        downloadVideo(url, file_name).run()

        srtName = '%s.srt'%name

        p = system("autosub -S en -D en %s -o %s" % (file_name,srtName))

        system('mv %s %s'%(srtName,srtPath))
        system('rm -rf %s*'%srtPath)

    except Exception:
        print ("失败")