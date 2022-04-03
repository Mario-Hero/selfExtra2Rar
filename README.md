# selfExtra2Rar 自解压文件转压缩文件

这是一个能把自解压文件（后缀为exe）转换成普通压缩文件的Python脚本。也能把压缩文件修改为正确的后缀。

能识别原本后缀为rar、zip、7z、bz2、gz的压缩文件。

## 依赖 

Python 3

## 用法 

把自解压文件拖入selfExtra2Rar.py脚本即可把该文件后缀修改为正确的压缩文件格式。

## 原理

每种文件都有固定的文件头。识别头，然后把压缩文件改成正确的后缀即可。对于后缀为exe的自解压文件，还会把程序部分的所有比特位置零。

## License

The project is released under MIT License.
