class ItemData():
    type_id = 0
    quantity = 0
    def __init__(self,item_id,quanitity):
        self.item_id = item_id
        self.quanitity = quanitity

class Basket():
    items = []

    def AddItem(self,type_id):
        for i in range(0,len(self.items)):
            if self.items[i].type_id == type_id:
                self.items[i].quantity +=1
                return True
        self.items.append(ItemData(type_id,1))
        return True
    def Clean(self):
        self.items = []

    


    
    