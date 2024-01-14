import pandas as pd
import numpy as np
import os
# mergefile_csv 合并csv GBK文件


def mfg(path):    # 参数为文件路径 路径样式为：E:\\年度医保基础数据\\2023年
    data = pd.DataFrame()
    files = os.listdir(path)
    for file in files:
        yb_data = pd.read_csv(f'{path}\\{file}', encoding='GBK')
        data = pd.concat([data,yb_data], axis=0, ignore_index=True)
    return data

# mergefile_utf 合并csv utf-8文件


def mfu(path):    # 参数为文件路径 路径样式为：E:\\年度医保基础数据\\2023年
    data = pd.DataFrame()
    files = os.listdir(path)
    for file in files:
        yb_data = pd.read_csv(f'{path}\\{file}', encoding='utf-8')
        data = pd.concat([data,yb_data], axis=0, ignore_index=True)
    return data

# mergefile_utf 合并excel文件


def mf(path):    # 参数为文件路径 路径样式为：E:\\年度医保基础数据\\2023年
    data = pd.DataFrame()
    files = os.listdir(path)
    for file in files:
        yb_data = pd.read_excel(f'{path}\\{file}')
        data = pd.concat([data,yb_data], axis=0, ignore_index=True)
    return data

# 对象测试

class Imcn:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c
    
    def mb(self):
        return self.a * self.b * self.c
    
def plus(number):
    a = 0
    for i in range(1,number):
        a = i + 1
    return a

imcn = 'I am Mark'