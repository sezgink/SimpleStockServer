from flask import Flask
from flask import request
import dataHolder
import basket

app = Flask(__name__)

basketInstance = basket.Basket()

@app.route('/')
def Hello():
    stock_dataframe = dataHolder.ReadData()
    top5 = stock_dataframe.head(5)
    return str(top5)

@app.route('/clean')
def Clean():
    stock_dataframe = dataHolder.CleanedStock()
    return str(stock_dataframe)

@app.route('/add',methods=['GET', 'POST'])
def AddItems():
    json_data = request.get_json()
    addResult = dataHolder.AddItems(json_data)
    
    return addResult

@app.route('/addToBasket',methods=['GET', 'POST'])
def AddToBasket():
    json_data = request.get_json()
    addResult = dataHolder.AddItems(json_data)
    
    return addResult

@app.route('/GetBasket')
def GetBasket():
    json_data = request.get_json()
    addResult = dataHolder.AddItems(json_data)
    
    return addResult