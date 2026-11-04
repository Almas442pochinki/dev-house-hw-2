from dataclasses import dataclass
import stock # from stock import Product, Electronics, Clothing, Books, Stock
from datetime import datetime

def main():
    print("-----------------------Warehouse Management System-----------------------")

    phone = stock.Electronics(code=1, name="Iphone", price=699.99, brand="BrandX", warranty_months=24)
    shirt = stock.Clothing(code=2, name="T-Shirt", price=19.99, brand="BrandY", size="M", fabric="Cotton")
    book = stock.Books(code=3, name="The Art of War", price=39.99, author="Sun Tzu", genre="Non-fiction")
    laptop = stock.Electronics(code=4, name="MacbookAir", price=1299.99, brand="BrandZ", warranty_months=12)
    stock_manager = stock.Stock()   
    stock_manager.add_product_to_stock(phone, quantity=10)
    stock_manager.add_product_to_stock(shirt, quantity=50)
    stock_manager.add_product_to_stock(book, quantity=25)
    stock_manager.add_product_to_stock(laptop, quantity=5)
    print(phone.get_product_info())
    print(shirt .get_product_info())
    print(book.get_product_info())
    print(laptop.get_product_info())
    print(f"Stock quantity for {phone.name}: {stock_manager.products[phone]}")
    print(f"Stock quantity for {shirt.name}: {stock_manager.products[shirt]}")
    print(f"Stock quantity for {book.name}: {stock_manager.products[book]}")
    print(f"Stock quantity for {laptop.name}: {stock_manager.products[laptop]}")
    print("------Display Stock Information------")
    stock_manager.show_stock()
    print('\n\n')
    stock_manager.remove_product_from_stock(phone, quantity=10)
    stock_manager.remove_product_from_stock(shirt, quantity=50)
    stock_manager.remove_product_from_stock(book, quantity=25)
    stock_manager.remove_product_from_stock(laptop, quantity=5)
    print("------Display Stock Information AFTER REMOVAL------")
    stock_manager.show_stock()
if __name__ == "__main__":
    main()