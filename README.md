# ubuntubar
Python、pandas 用于导入数据表并合并的模块
使用前需要先导入模块
import mymodule as mm

使用时有三个函数
如果数据文件是xls\xlsx：
data = mm.mf('数据文件目录地址')
如果是utf-8的csv文件：
data = mm.mfu('数据文件目录地址')
如果是GBK的csv文件：
data = mm.mfg('数据文件目录地址')

注：在合并csv时要保证所有文件的编码统一。
