from flask import Flask
from flask import request
import dataHolder
import basket

app = Flask(__name__)

basketInstance = basket.Basket()

@app.route('/stock')
def Stock():
    stock_dataframe = dataHolder.ReadData()
    top5 = stock_dataframe.head(5)
    return str(stock_dataframe)
    # return str(top5)

@app.route('/clean')
def Clean():
    stock_dataframe = dataHolder.CleanedStock()
    return str(stock_dataframe)

@app.route('/add',methods=['GET', 'POST'])
def AddItems():
    json_data = request.get_json()
    addResult = dataHolder.AddItems(json_data)
    
    return addResult
@app.route('/createitem',methods=['GET', 'POST'])
def CreateItem():
    json_data = request.get_json()
    addResult = dataHolder.CreateItemData(json_data)
    
    return addResult

@app.route('/addtobasket',methods=['GET', 'POST'])
def AddToBasket():
    global basketInstance
    json_data = request.get_json()
    basketInstance.AddItem(json_data["type_id"])
    return basketInstance.ToJson()

@app.route('/getbasket')
def GetBasket():
    global basketInstance
    json_data = basketInstance.ToJson()    
    return json_data

@app.route('/checkoutbasket',methods=['GET', 'POST'])
def CheckoutBasket():
    global basketInstance
    json_data = basketInstance.ToJsonObject()
    dataHolder.RemoveItems(json_data)
    basketInstance.Clean()    
    return json_data

@app.route('/cleanbasket')
def CleanBasket():
    global basketInstance
    basketInstance.Clean()  
    return basketInstance.ToJson() 