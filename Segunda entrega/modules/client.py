#Introduction for the store
print("Hi, My name is Ale and i need some data for your user registry because we are sure you wanna love this!.")

#global var
username = input("Please add your name: ")
mail = input("Please add your e-mail: ")
phone_number = input("Please add your phone_number: ")
delivery_address = input("Please add your delivery_address: ")

class Client:
    pass
    def __init__(self, name, mail, phone_number, delivery_address):
        self.name = name
        self.mail = mail
        self.phone_number = phone_number
        self.delivery_address = delivery_address

    def show_info(self):
        print(f"your name is: << {self.name} >>")
        print(f"your email is: << {self.mail} >>")
        print(f"you phone number is: << {self.phone_number} >>")
        print(f"Your delivery address is: << {self.delivery_address} >> \n")

#test module
your_data = Client(username, mail, phone_number,delivery_address)
your_data.show_info()

#my_user_client = Client("Alejandra","kblmrtnz@gmail.com","952555744","Duble Almeyda 1818")
#my_user_client.show_info()
