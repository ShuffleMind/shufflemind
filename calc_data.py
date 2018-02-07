def calc_data(typeAgg, stock):
    #avalia o calculo para retornar a agragacao
    df_stock = pd.DataDrame(stock)
    if typeAgg == 'Média':
        df_stock = df_stock['Close'].mean()
        return df_stock
    elif typeAgg == 'Máximo':
        df_stock = df_stock['Close'].max()
        return df_stock
    elif typeAgg == 'Mínimo':
        df_stock = df_stock['Close'].min()
        return stock
