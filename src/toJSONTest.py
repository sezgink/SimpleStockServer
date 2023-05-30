from basket import Basket

basket = Basket()

basket.AddItem(2)
basket.AddItem(2)
basket.AddItem(2)
basket.AddItem(2)
basket.AddItem(2)

print(str(basket.ToJson()))
