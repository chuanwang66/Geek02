import pandas as pd
import os

def load_df(file_name):
    # 读取数据
    data_path = os.path.join('D:\\workspace\\python\\akshare\\code07', file_name)
    df = pd.read_csv(data_path)
    # 将日期列转换为datetime类型
    df['日期'] = pd.to_datetime(df['日期'])
    return df