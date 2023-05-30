import pandas as pd
import os.path

stock_data_columns = ["type_id","quantity"]
stock_data_adress = "stockData.csv"

def CreateNewData():
    newDataFrame = pd.DataFrame(columns=stock_data_columns)
    WriteData(newDataFrame,stock_data_adress)
    return newDataFrame

def ReadData():
    print(os.getcwd())
    fileExist = os.path.isfile(stock_data_adress)
    print("File exits:",str(fileExist))
    if fileExist:
        dataFrame = pd.read_csv(stock_data_adress)
    else:
        dataFrame = CreateNewData()
    return dataFrame

def WriteData(dataFrame : pd.DataFrame,dataAdress):
    dataFrame.to_csv(dataAdress,index=False)

def FindAndAddItem(df : pd.DataFrame,typeId:int,quantity : int):
    if (df['type_id'] == typeId).any():
        df.loc[df['type_id'] == typeId, 'quantity'] += quantity
    else:
        new_row = pd.DataFrame({'type_id': [typeId], 'quantity': [quantity]} )
        df = pd.concat([df,new_row],ignore_index=True)
    return df

def FindAndRemoveItem(df : pd.DataFrame,typeId:int,quantity : int):
    if (df['type_id'] == typeId).any():
        df.loc[df['type_id'] == typeId, 'quantity'] -= quantity
    else:
        new_row = pd.DataFrame({'type_id': [typeId], 'quantity': [-quantity]} )
        df = pd.concat([df,new_row],ignore_index=True)
    return df

def AddItems(itemsJSON):
    # print(itemsJSON)
    stock_data = ReadData()
    for item in itemsJSON["items"]:
        stock_data = FindAndAddItem(stock_data,item["type_id"],item["quantity"])
    WriteData(stock_data,stock_data_adress)
    return str(stock_data.head(5))
def RemoveItems(itemsJSON):
    print(itemsJSON)
    stock_data = ReadData()
    for item in itemsJSON["items"]:
        stock_data = FindAndRemoveItem(stock_data,item["type_id"],item["quantity"])
    WriteData(stock_data,stock_data_adress)
    return str(stock_data.head(5))

def CleanedStock():
    return CreateNewData()
    




    
