class computer:
    __maxprice=50000
    def sell(self):
        print("selling price is",computer.__maxprice)
    def changemaxprice(self,price):
        computer.__maxprice=price
o=computer()
o.sell()
o.changemaxprice(30000)
o.sell()