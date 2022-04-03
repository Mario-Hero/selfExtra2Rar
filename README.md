# selfExtra2Rar 自解压文件转压缩文件

这是一个能把自解压文件（后缀为exe）转换成普通压缩文件的Python脚本。

能识别原本后缀为rar、zip、7z、bz2、gz的压缩文件。

## 依赖 

Python 3

## 用法 

把自解压文件拖入selfExtra2Rar.py脚本即可在自解压文件所在文件夹生成其原本的压缩文件。

## 原理

每种文件都有固定的文件头。识别头，然后把后面的所有内容写入一个新文件即可。**但是目前的方法并不高效，写入速度取决于硬盘速度。如果谁有能直接切割文件的方法希望能发邮件或者在知乎上告诉我。**

## License

The project is released under MIT License.