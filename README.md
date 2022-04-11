# selfExtra2Rar 自解压文件转压缩文件

这是一个能把自解压文件（后缀为exe）转换成普通压缩文件的Python脚本。也能把压缩文件修改为正确的后缀。

能识别原本后缀为rar、zip、7z、bz2、gz的压缩文件。

This is a Python script which can convert self extracting files (with extension '.exe') into ordinary compressed files. It can also modify the compressed file to the correct extension.
It can identify compressed files with extension: rar, zip, 7z, bz2 and gz.

## 依赖 Depedency

Python 3

## 用法 Usage

把自解压文件拖入selfExtra2Rar.py脚本即可把该文件后缀修改为正确的压缩文件格式。

Drag a self extracting file into selfExtra2Rar.py, then it can modify the file extension to the correct one.

## 原理 Princples

每种文件都有固定的文件头。识别头，然后把压缩文件改成正确的后缀即可。对于后缀为exe的自解压文件，还会把程序部分的所有比特位置零。

Each file has a fixed header. This script can Identify the header, and then change the compressed file to the correct extension. For the self extracting file with the extension '.exe', all bits of the program will be set as zero.

## License

The project is released under MIT License.
