import pandas as pd
import pandas_datareader as pdr

def get_stock(stock):
    stockDf = pdr.get_data_yahoo(stock)
    return stockDf

def mergeStock(stockList,start_dt,end_dt):
    dates = pd.date_range(start_dt, end_dt)
    df = pd.DataFrame(index = dates)
    for symbol in stockList:
        fildsToDrop = ['Open','High','Low','Close','Volume']
        dfTemp = pd.DataFrame(get_stock(symbol))  
        dfTemp = dfTemp.rename(columns={'Adj Close': symbol})
        dfTemp = dfTemp.drop(fildsToDrop,axis=1)  
        df = df.join(dfTemp, how='inner') 
    return df
        
        
    
    
    
    
