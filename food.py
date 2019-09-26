# -*- coding: utf-8 -*-

from ShortPackage.downloadVideo import downloadVideo
import os
from os import system
from dotenv import load_dotenv
load_dotenv()



class food:

    def __init__(self):

        print ("开始视频")


    def run(self):


        i = 0

        while True and i <100:
            try:
                self.downAndGetSrt()
            except Exception:
                i+=1


        print ("运行数据")


    def downAndGetSrt(self):

        path = 'download'
        srtPath = './'

        name = '50个人尝试制作大蒜酱'
        url = 'https://video.epicurious.com/watch/50-people-try-to-make-garlic-paste?c=series'

        file_name = '%s/%s.mp4' % (path, name)


        try:
            downloadVideo(url, file_name).run()
            srtName = '%s/%s.srt' % (path, name)
            p = system("autosub -S en -D en %s -o %s" % (file_name, srtName))
            system('mv %s %s' % (srtName, srtPath))
            system('rm -rf %s/*' % path)
            system('git add .')
            system('git commit -a -m "%s"' % name)
            system('git push"')
        except Exception:
            print ("失败")





if __name__ == '__main__':
        food().run()