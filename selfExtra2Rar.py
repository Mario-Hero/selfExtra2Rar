#!/usr/bin/python3
# _*_ coding: UTF-8 _*_

# Created by Mario Chen, 31.03.2022, Shenzhen
# My Github site: https://github.com/Mario-Hero

import os
import time
import sys


WRITE_TO_NEW_FILE = False  # 为真时，新建一个压缩文件。为假时，把原来的文件修改为正确的后缀，并把程序的部分全部置零。

READ_SIZE = int(1024 * 1024 * 16)  # 16MB
FILE_EXT = \
    [['rar', b'Rar!'],
     ['zip', b'PK'],
     ['7z', b"7z\xbc\xaf'\x1c"],
     ['bz2', b'BZh'],
     ['gz', b'1f8b']]


def selfExtract2Rar(selfExtractFile):
    getHead = False
    seekTarget = 0
    realExt = ''
    with open(selfExtractFile, 'rb') as f:
        while True:
            data = f.read(16)
            # print(data)
            # print(data.hex())
            for ext in FILE_EXT:
                if data.startswith(ext[1]):
                    print('Get extension: ' + ext[0])
                    realExt = ext[0]
                    getHead = True
                    break
            if (not data) or getHead:
                break
            else:
                seekTarget += 16
                if seekTarget > 400000:
                    break
    if getHead:
        normalFile = os.path.splitext(selfExtractFile)[0] + '.' + realExt
        i = 1
        while os.path.exists(normalFile):
            normalFile = os.path.splitext(selfExtractFile)[0] + str(i) + '.' + realExt
            i += 1
        if WRITE_TO_NEW_FILE:
            originalFileSize = os.path.getsize(selfExtractFile) - seekTarget
            print('Output as: ' + normalFile)
            startTime = time.time()
            with open(normalFile, 'wb') as fb:
                if READ_SIZE:
                    with open(selfExtractFile, 'rb') as f:
                        f.seek(seekTarget)
                        readI = 0
                        while True:
                            data = f.read(READ_SIZE)
                            if data:
                                readI += 1
                                fb.write(data)
                                i = int(readI * READ_SIZE / originalFileSize * 100)
                                print("\r", end="")
                                print("Progress: {}%: ".format(i), "▋" * (i // 2), end="")
                                sys.stdout.flush()
                            else:
                                break
                else:
                    with open(selfExtractFile, 'rb') as f:
                        f.seek(seekTarget)
                        fb.write(f.read())
            endTime = time.time()
            allTime = round(endTime - startTime, 3)
            print('\nCost: ' + str(allTime) + 's')
        else:
            if seekTarget > 0:
                with open(selfExtractFile, 'rb+') as f:
                    while seekTarget > 0:
                        f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                        seekTarget -= 16
            os.rename(selfExtractFile, normalFile)
    else:
        print('Cannot get extension of ' + selfExtractFile)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            selfExtract2Rar(file)
        # os.system('pause')
