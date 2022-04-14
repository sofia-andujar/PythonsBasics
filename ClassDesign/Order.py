from Product import Product

# This class is created afterwards as it contains objects of type Product

class Order():
    
    orderCounter = 0
    
    def __init__(self,products):
        self._id = Order.newOrder()
        self._products = list(products)
        
    @classmethod
    def newOrder(cls):
        cls.orderCounter += 1
        return cls.orderCounter
    
    def add_product(self,product):
        self._products.append(product)
        
    def totalPrice(self):
        total = 0
        for product in self._products:
            total += product.price
        return total
    
    def __str__(self) -> str:
        string = ''
        for product in self._products:
            string += product.__str__() + '\n'
        return f'Order ID: {self._id}, Products: \n{string}'
    
    @property
    def id(self):
        return self._id
    
if __name__ == '__main__':
    pr1 = Product('t-shirt',8)
    pr2 = Product('shorts',12)
    pr3 = Product('jeans',18)
    pr4 = Product('jumper',15)
    
    ord1 = Order([pr1, pr2, pr3, pr4])
    print(ord1)
    print(f'Total price of order {ord1.id} is: {ord1.totalPrice()}')
    
    ord2 = Order([pr4,pr2,pr1,pr3,Product('socks',10)])
    print(ord2)
    print(f'Total price of order {ord2.id} is: {ord2.totalPrice()}')