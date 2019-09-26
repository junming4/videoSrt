# -*- coding: utf-8 -*-

from ShortPackage.downloadVideo import downloadVideo
import os
from os import system
from dotenv import load_dotenv
load_dotenv()


import sys


if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')



class food:

    def __init__(self):

        print ("开始视频")


    def run(self):

        self.downAndGetSrt()
        print ("运行数据")


    def downAndGetSrt(self):

        path = 'download'
        srtPath = '/home/www/var/videoSrt/'


        urlList = [
            'https://video.epicurious.com/watch/50-people-try-to-slice-an-avocado?c=series 50个人尝试切鳄梨',
            'https://video.epicurious.com/watch/50-people-try-to-slice-a-mango?c=series 50个人尝试切芒果',
            'https://video.epicurious.com/watch/50-people-try-to-hone-a-knife?c=series 50个人试图磨刀',
            'https://video.epicurious.com/watch/50-people-try-to-cut-carrot-sticks?c=series 50个人尝试切胡萝卜',
            'https://video.epicurious.com/watch/50-people-try-to-chop-deseed-a-pepper?c=series 50个人试图剁成辣椒',
            'https://video.epicurious.com/watch/50-people-try-to-slice-an-apple-for-pie?c=series 50个人尝试切苹果馅饼',
            'https://video.epicurious.com/watch/50-people-try-to-dice-an-onion?c=series 50个人尝试将洋葱切丁',
            'https://video.epicurious.com/watch/50-people-try-to-cut-pineapple-rings?c=series 50个人尝试切割菠萝戒指',
            'https://video.epicurious.com/watch/50-people-try-to-peel-and-cube-a-potato?c=series 50个人尝试去皮和切块马铃薯',
            'https://video.epicurious.com/watch/50-people-try-to-remove-artichoke-hearts?c=series 50个人试图去除洋蓟心',
            'https://video.epicurious.com/watch/50-people-try-to-make-scrambled-eggs?c=series 50个人尝试制作炒鸡蛋',
            'https://video.epicurious.com/watch/50-people-try-to-shuck-corn?c=series 50人试图去皮玉米',
            'https://video.epicurious.com/watch/50-people-try-to-crack-a-coconut?c=series 50个人尝试破解椰子',
            'https://video.epicurious.com/watch/50-people-try-to-make-a-vinaigrette?c=series 50个人尝试制作油醋汁',
            'https://video.epicurious.com/watch/50-people-try-to-chop-and-deseed-a-jalapeno?c=series 50个人试图砍下墨西哥辣椒',
            'https://video.epicurious.com/watch/50-people-try-to-fillet-a-fish?c=series 50个人尝试去鱼片',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-juice-a-lemon?c=series 50个人尝试榨柠檬汁',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-make-brown-butter?c=series 50人尝试制作黄油',
            'https://video.epicurious.com/watch/50-people-try-to-devein-shrimp?c=series 50个人尝试去皮和去虾',
            'https://video.epicurious.com/watch/50-people-try-to-make-a-french-omelette?c=series 50个人尝试制作法国煎蛋',
            'https://video.epicurious.com/watch/50-people-try-to-cut-a-watermelon?c=series 50个人尝试切西瓜',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-make-pancakes?c=series 50个人尝试制作煎饼',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-make-a-peanut-butter-and-jelly-sandwich?c=series 50个人尝试制作花生酱和果冻...',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-toss-pizza-dough?c=series 50个人尝试扔披萨面团',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-peel-a-tomato?c=series 50个人尝试去皮番茄',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-soft-boil-an-egg?c=series 50个人尝试煮鸡蛋',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-peel-a-hardboiled-egg?c=series 50个人尝试去皮煮鸡蛋',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-peel-a-kiwi?c=series 50个人尝试去皮猕猴桃',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-make-a-martini?c=series 50人尝试制作马提尼酒',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-make-whipped-cream?c=series 50个人尝试制作奶油',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-identify-vegetables?c=series 50个人猜水果和蔬菜',
            'https://video.epicurious.com/watch/50-people-try-to-make-sushi?c=series 50个人尝试做寿司',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-make-a-grilled-cheese-sandwich?c=series 50个人尝试制作烤奶酪三明治',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-cut-a-butternut-squash?c=series 50个人尝试切割胡桃南瓜',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-poach-an-egg?c=series 50个人尝试煮鸡蛋',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-make-fried-chicken?c=series 50个人尝试做炸鸡',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-open-a-bottle-of-wine?c=series 50个人尝试打开一瓶酒',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-chop-lettuce?c=series 50个人尝试切生菜',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-identify-shellfish?c=series 50个人试图识别贝类',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-shuck-an-oyster?c=series 50个人试图去掉牡蛎',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-crack-a-walnut?c=series 50个人试图破解核桃',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-identify-different-cuts-of-beef?c=series 50个人试图识别牛肉块',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-cut-and-prep-an-eggplant?c=series 50个人尝试切割和准备茄子',
            'https://video.epicurious.com/watch/50-person-prep-challenge-best-fails-in-50-people-try-200?c=series 50人尝试中最多失败（200多次失败）',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-make-a-quesadilla?c=series 50人尝试制作墨西哥玉米饼',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-identify-spices?c=series 50个人尝试识别6种香料',
            'https://video.epicurious.com/watch/50-person-prep-challenge-50-people-try-to-mince-parsley?c=series 50个人尝试切碎欧芹'
        ]

        i = 0

        for urlText in urlList:
            url,name =  urlText.split(' ')

            file_name = '%s/%s.mp4' % (path, name)

            srtName = '%s/%s.srt' % (path, name)

            if os.path.isfile(srtName):
                continue


            try:
                # downloadVideo(url, file_name).run()

                p = system("autosub -S en -D en %s -o %s" % (file_name, srtName))
                system('mv %s %s' % (srtName, srtPath))
                system('rm -rf %s/*' % path)
                system('git add .')
                system('git commit -a -m %s' % name)
                system('git push')
            except Exception:
                i +=1
                print ("fail num:%d"%i)







if __name__ == '__main__':
        food().run()