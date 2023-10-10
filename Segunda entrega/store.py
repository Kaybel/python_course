print("Thanks for the register.")

#global var

#product = input("Please add your name: ")
#price = input("Please add your e-mail: ")
#category = input("Please add your phone_number: ")
#amount = input("Please add your delivery_address: ")

class Store:
    pass
    def __init__(self, product, price, category, amount):
        self.ItemStore=[]
        self.product = product
        self.price = price
        self.category = category
        self.amount = amount        
    def __str__(self) -> str:
        return f"This it's the first move into a organized life, This is the item you wanna set in the register: << {self.product} >>, the price for this article is: << {self.price} >>, the category is: << {self.category} >>, and you have this amount of items: << {self.amount} >> \n"
    
#product = Store(product, price, category, amount)
product2 = Store("One Piece Tomo 15","10990","Aventura", "5")

shopping_car = []

def add_product(product, price):
    shopping_car.append(
        {
            "product": product, 
            "price": price
        }
    )
    print(f"The product << {product} >> was added to the shopping car.")

def show_shopping_car():
    if not shopping_car:
        print("you dont have any data to show.")
    else:
        print("The Shopping Car have the following data: ")
        total_price = 0
        for item in shopping_car:
            print(f"Product << {item['product']} >> - Price: << ${item['price']} >>")
            total_price += item['price']
        print(f"The total price is: ${total_price}")

while True:
    print("Select one number for the following options.")
    print("\n1. Add product to the shopping car")
    print("2. Show shopping car")
    print("3. LogOut")
    
    option = input("Selecciona una opción: ")
    
    if option == "1":
        product = input("Please digit the product: ")
        price = float(input("Please digit the price: "))
        add_product(product, price)
    elif option == "2":
        show_shopping_car()
    elif option == "3":
        break
    else:
        print("No valid option. Please, select a valid option.")
