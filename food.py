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

        self.downAndGetSrt()
        print ("运行数据")


    def downAndGetSrt(self):

        path = 'download'
        srtPath = '/home/www/var/videoSrt/'


        '''urlList = [
            {
                'url': 'https://video.epicurious.com/watch/50-people-try-to-make-garlic-paste?c=series',
                'name':'50个人尝试制作大蒜酱'
            },
            {
                'url': 'https://video.epicurious.com/watch/50-people-try-to-separate-an-egg?c=series',
                'name': '50个人试图分开蛋清和蛋黄'
            },
            {
                'url': 'https://video.epicurious.com/watch/50-people-try-to-slice-an-avocado?c=series',
                'name': '50个人尝试切鳄梨'
            },
            {
                'url': 'https://video.epicurious.com/watch/50-people-try-to-slice-a-mango?c=series',
                'name':'50个人尝试切芒果'
            },
            {
                'url': 'https://video.epicurious.com/watch/50-people-try-to-hone-a-knife?c=series',
                'name': '50个人试图磨刀'
            },
            {
                'url': 'https://video.epicurious.com/watch/50-people-try-to-cut-carrot-sticks?c=series',
                'name': '50个人尝试切胡萝卜'
            },
            {
                'url': 'https://video.epicurious.com/watch/50-people-try-to-chop-deseed-a-pepper?c=series',
                'name': '50个人试图剁成辣椒'
            },
            {
                'url': 'https://video.epicurious.com/watch/50-people-try-to-slice-an-apple-for-pie?c=series',
                'name': '50个人尝试切苹果馅饼'
            }
        ]'''


        name = '50个人尝试制作大蒜酱'
        url = 'https://video.epicurious.com/watch/50-people-try-to-make-garlic-paste?c=series'

        file_name = '%s/%s.mp4' % (path, name)

        system('git commit -a -m %s' % name)
        system('git push')


        '''try:
            downloadVideo(url, file_name).run()
            srtName = '%s/%s.srt' % (path, name)
            p = system("autosub -S en -D en %s -o %s" % (file_name, srtName))
            system('mv %s %s' % (srtName, srtPath))
            system('rm -rf %s/*' % path)
            system('git add .')
            system('git commit -a -m %s' % name)
            system('git push')
        except Exception:
            print ("失败")'''





if __name__ == '__main__':
        food().run()