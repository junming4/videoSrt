# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import string

import youtube_dl
from os import rename


class myLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class downloadVideo:

    def __init__(self, url, fileName):
        self.url = url
        self.fileName = fileName

        print ("下载视频")

    #修改名字
    def renameMp4(self, d):
        if d['status'] == 'finished':
            print (d)

            file_name = self.fileName
            rename(d['filename'], file_name)
            print('下载完成{}'.format(file_name))

            print('Done downloading, now converting ...')

    def run(self):

        if string.find(self.url, 'http') == -1:
           url = 'https://www.youtube.com/results?search_query=%s'%self.url
           ydl_opts = {
               'verbose': True,
               'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
               'format': 'best',  # choice of quality
               'extractaudio': True,  # only keep the audio
               # 'videoformat' : "mp4",      # convert to mp4
               'outtmpl': '%(title)s.%(ext)s',  # name the file the title of the video
               # 'max_downloads':1,
               # '_num_downloads':1,
               'filesize': 8388608,
               'noplaylist': True,  # only download single song, not playlist
               #'playliststart': '1',
               'playlist_items': '1',
               'logger': myLogger(),
               'progress_hooks': [self.renameMp4],
           }
        else:
            ydl_opts = {
                'verbose': True,
                'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
                'format': 'best',  # choice of quality
                'extractaudio': True,  # only keep the audio
                # 'videoformat' : "mp4",      # convert to mp4
                'outtmpl': '%(title)s.%(ext)s',  # name the file the title of the video
                # 'max_downloads':1,
                # '_num_downloads':1,
                'filesize': 8388608,
                'noplaylist': True,  # only download single song, not playlist
                'playlist_items': '1',
                'logger': myLogger(),
                'progress_hooks': [self.renameMp4],
            }
            url = self.url

        print (ydl_opts)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])