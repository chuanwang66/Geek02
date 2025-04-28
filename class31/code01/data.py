from typing import List
import akshare as ak
import pandas as pd

def save_data(codes:List[str], start_date:str, end_date:str):
     all_data= pd.DataFrame()
     for code in codes:
         df=load_data(code,start_date,end_date)
         all_data=pd.concat([all_data, df],axis=0)
     filename="{}_{}.csv".format(start_date,end_date)
     all_data.to_csv("D:\\workspace\\python\\akshare\\code04\\data\\{}".format(filename))
     print("保存所有日线数据完成,文件名是:{}".format(filename))

def load_data(symbol, start_date, end_date):
    df = ak.stock_zh_a_hist(
        symbol=symbol, 
        period="daily", 
        start_date=start_date, 
        end_date=end_date, 
        adjust="qfq"
    )

    df['日期'] = pd.to_datetime(df['日期'])
    df.set_index('日期', inplace=True)
    df.sort_index(ascending=False, inplace=True)

    return df

if __name__ == "__main__":
    save_data(["300750", "600519"], "20250407", "20250411")