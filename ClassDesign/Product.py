# This class doesn't depend on the others, so it is the first we create

class Product:
    
    productCounter = 0
    
    def __init__(self,name,price):
        self._id = Product.newProduct()
        self._name = name
        self._price = price
        
    @classmethod
    def newProduct(cls):
        cls.productCounter += 1
        return cls.productCounter
    
    def __str__(self) -> str:
        return f'Product ID: {self._id}, Name: {self._name}, Price: {self._price} €'
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,price):
        self._price = price
    
    
if __name__ == '__main__':
    pr1 = Product('t-shirt',8)
    print(pr1)
    pr2 = Product('shorts',12)
    print(pr2)