import pandas as pd
import os.path
import numpy as np
import math
stock_data_columns = ["type_id","quantity","price","name"]
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

def FindOrCreateItem(df : pd.DataFrame, itemData : dict):
    if False: #TODO: Constraits for creating item
        print(False)
    # if (df['type_id'] == typeId).any() & False:
        # df.loc[df['type_id'] == typeId, 'quantity'] += quantity
    else:
        isEmpty = maxTypeId = df.loc[df['type_id']].empty
        if isEmpty:
            maxTypeId = 0
        else:
            maxTypeId = int(df.type_id.max()) + 1
        new_row = pd.DataFrame({'type_id': [maxTypeId], 'quantity': [0],'price':[itemData["price"]] ,'name':[itemData["name"]]} )
        df = pd.concat([df,new_row],ignore_index=True)
    return df

def AddItems(itemsJSON):
    # print(itemsJSON)
    stock_data = ReadData()
    for item in itemsJSON["items"]:
        stock_data = FindAndAddItem(stock_data,item["type_id"],item["quantity"])
    WriteData(stock_data,stock_data_adress)
    return str(stock_data.head(5))

def FindAndUpdatePrice(df : pd.DataFrame,typeId:int,price : int):
    if (df['type_id'] == typeId).any():
        df.loc[df['type_id'] == typeId, 'price'] += price
    return df

def CreateItemData(itemData):
    stock_data = ReadData()
    stock_data = FindOrCreateItem(stock_data,itemData)
    WriteData(stock_data,stock_data_adress)
    return str(stock_data.head(5))

def UpdateItemPrice(itemData):
    stock_data = ReadData()
    stock_data = FindAndUpdatePrice(stock_data,itemData["type_id"],itemData["price"])
    WriteData(stock_data,stock_data_adress)
    return str(stock_data.head(5))

def GetPriceDict():
    stock_data = ReadData()
    stock_data = stock_data[["type_id","price"]]  # Selecting only the type_id and price columns
    stock_data_dict = stock_data.to_dict('records')
    return stock_data_dict

def RemoveItems(itemsJSON):
    print(itemsJSON)
    stock_data = ReadData()
    for item in itemsJSON["items"]:
        stock_data = FindAndRemoveItem(stock_data,item["type_id"],item["quantity"])
    WriteData(stock_data,stock_data_adress)
    return str(stock_data.head(5))

def CleanedStock():
    return CreateNewData()
    




    
