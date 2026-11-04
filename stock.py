from datetime import datetime
from enum import Enum
from abc import ABC, abstractmethod
from dataclasses import dataclass

class WarehouseError(Exception):
    pass

class ProductNotFound(WarehouseError): # potom
    pass

class InvalidQuantity(WarehouseError):
    pass

class OutOfStock(WarehouseError):
    pass

class InvalidProductCode(WarehouseError):
    pass

class TimestampMixin:
    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ProductStatus(Enum):
    IN = "IN STOCK"
    OUT = "OUT OF STOCK"

class ProductType(Enum):
    ELECTRONICS = "Electronics"
    CLOTHING = "Clothing"
    BOOKS = "Books"

@dataclass(frozen=True)
class Product(ABC):
    code: int
    name: str
    price: float

    @abstractmethod
    def get_product_info(self) -> str:
        pass

@dataclass(frozen=True)
class Electronics(Product):
    brand: str
    warranty_months: int
    def get_product_info(self) -> str:
        return f"Electronics - Code: {self.code}, Name: {self.name}, Brand: {self.brand}, Price: {self.price} USD, Warranty: {self.warranty_months} months."

@dataclass(frozen=True)
class Clothing(Product):
    brand: str
    size: str 
    fabric: str
    def get_product_info(self) -> str:
        return f"Clothing - Code: {self.code}, Name: {self.name}, Brand: {self.brand}, Size: {self.size}, Fabric: {self.fabric}, Price: {self.price} USD."

@dataclass(frozen=True)
class Books(Product):
    author: str
    genre: str
    def get_product_info(self) -> str:
        return f"Books - Code: {self.code}, Name: {self.name}, Author: {self.author}, Genre: {self.genre}, Price: {self.price} USD."



class Stock: 
    products: dict[Product, int]
    catalogue: dict[int, Product]
    quantity: int
    status: ProductStatus
    
    def __init__(self):
        self.catalogue: dict[int, Product] = {} # code - product
        self.products: dict[Product, int] = {} # product - quantity 
        self.quantity = 0

    def add_product_to_stock(self, product: Product, quantity: int = 1):
        if product in self.products:
            self.products[product] += quantity
            self.catalogue[product.code] = product
        else:
            self.products[product] = quantity
        print(f"Added {quantity} units of {product.name} to stock.")

    def remove_product_from_stock(self, product: Product, quantity: int = 1):
        if product in self.products and self.products[product] >= quantity:
            self.products[product] -= quantity
            if self.products[product] <= 0:
                self.products[product] = 0
        else:
            raise InvalidQuantity("Invalid quantity specified. Please check the quantity and try again.")
        print(f"Removed {quantity} units of {product.name} from stock.")

    def get_product_quantity(self, product: Product) -> int:
        return self.products.get(product, 0)

    def show_stock(self):
        print('Current Stock Information:')
        for product, quantity in self.products.items():
            if quantity > 0: 
                status = ProductStatus.IN
            else: status = ProductStatus.OUT
            print(f"{product.get_product_info()} | Quantity: {quantity} | Status: {status}")

    