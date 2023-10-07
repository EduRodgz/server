# global variables
from config import developer




# functions

def print_menu():
    print('---------------------')
    print('---- Python 2023 ----')
    print('---------------------')

def dictionary_1():
    pet = {
        "type": "rabbit",
        "name": "Bruno",
        "color": "Black",
        "age": "2"
    }
    print(pet)
    #read
    print("My pet is: " + pet["name"])
    #modify
    pet["age"] = 3
    # add
    pet["size"] = "small"
    # remove
    pet.pop("type")
    print(pet)

def dictionary_2():
    print(developer)
    print(developer["first"] + " " + developer["last"])
    address = developer["address"]
    print(address)
    print(address["num"] + " " + address["street"] + " " + address["city"])


print_menu()
dictionary_1()
dictionary_2()