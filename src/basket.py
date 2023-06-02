import json
import dataHolder

class ItemData():
    type_id = 0
    quantity = 0
    unit_price = 0
    def __init__(self,item_id,quantity):
        self.type_id = item_id
        self.quantity = quantity

class Basket():
    items = []

    def AddItem(self,type_id):
        for i in range(0,len(self.items)):
            if self.items[i].type_id == type_id:
                self.items[i].quantity +=1
                return True
        self.items.append(ItemData(type_id,1))
        # print(self.ToJson())
        return True
    def Clean(self):
        self.items = []
    def ToJson(self):
        price_dict = dataHolder.GetPriceDict()
        for item in self.items:
            item.unit_price = price_dict[item.type_id]
        items_array = [item.__dict__ for item in self.items]
        basketDict = {"items":items_array}
        # print(basketDict)
        return json.dumps(basketDict)
    def ToJsonObject(self):
        price_dict = dataHolder.GetPriceDict()
        for item in self.items:
            item.unit_price = price_dict[item.type_id]
        items_array = [item.__dict__ for item in self.items]
        basketDict = {"items":items_array}
        # print(basketDict)
        return basketDict