# -*- coding: utf-8 -*-

from ShortPackage.downloadVideo import downloadVideo
import os
from os import system
from dotenv import load_dotenv
load_dotenv()

import pymongo


class food:

    def __init__(self):

        print ("开始视频")


    def run(self):

        print ("运行数据")


    def downAndGetSrt(self):

        path = 'download'
        srtPath = os.getenv('VIDEO_SRT_PATH')

        myclient = pymongo.MongoClient("mongodb://47.104.77.182:27017/")
        mydb = myclient["video"]
        mycol = mydb["food"]

        while mycol.find_one({'status': 0}) != None:
            data = mycol.find_one({'status': 0})

            name = data['name']

            myquery = {"_id": data['_id']}

            file_name = '%s/%s.mp4' % (path, name)

            url = data['url']
            try:
                downloadVideo(url, file_name).run()
                srtName = '%s/%s.srt' % (path, name)
                p = system("autosub -S en -D en %s -o %s" % (file_name, srtName))
                system('mv %s %s' % (srtName, srtPath))
                system('rm -rf %s/*' % path)
                system('cd %s' % srtPath)
                '''system('git add .')
                system('git commit -a -m "%s"' % name)
                system('git push"')'''
                setx = {"$set": {'status': 1}}
            except Exception:
                print ("失败")
                setx = {"$set": {'status': -1}}

            mycol.update_one(myquery, setx)


if __name__ == '__main__':
        food().run()