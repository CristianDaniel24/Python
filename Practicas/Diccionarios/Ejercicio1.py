fruits = {
    "Apple": {
        "Characteristics": ["red", "sweet","crunchy"],
        "Information": {"Price:":1.40,"stock":30}
    },
    "Orange": {
        "Characteristics": ["orange", "acidic","juicy"],
        "Information": {"Price:":2.20,"stock":25}
    },
    "Banana": {
        "Characteristics": ["yellow", "gentle","sweet"],
        "Information": {"Price:":3.0,"stock":32}
    },
    "Grape": {
        "Characteristics": ["dwelling", "sweet","small"],
        "Information": {"Price:":2.40,"stock":15}
    },
    "Pear": {
        "Characteristics": ["green", "sweet","juicy"],
        "Information": {"Price:":1.60,"stock":10}
    },
}

def addFruit():
    name = input("\nEnter the name of the fruit:").capitalize()
    characteristics = input("Enter the characteristics separated by commas (eg: red, sweet, crunchy): ").split(", ")
    price = float(input("Enter the price:"))
    stock = int(input("Enter the stock:"))
    fruits[name] = {
        "Characteristics": characteristics,
        "Information": {"price":price, "stock":stock}
    }
    print(f"The fruit {name} added successfully\n")

def editFruit():
    name = input("\nEnter the new name for edit:").capitalize()
    if name in fruits:
        characteristics = input("Enter the new Characteristics separated by commas:").split(", ")
        price = float(input("Enter the new price:"))
        stock = int(input("Enter the new stock:"))
        fruits[name] = {
            "Characteristics": characteristics,
            "Information": {"price": price, "stock": stock}
        }
        print(f"The fruit {name} edit successfully\n")
    else:
        print(f"The fruit {name} does not exist\n")

def deletedFruit():
    name = input("\nEnter the name for deleted:").capitalize()
    if name in fruits:
        del fruits[name]
        print(f"\nThe fruit {name} deleted successfully\n")
    else:
        print(f"\nThe fruit {name} does not exist\n")

def printFruits():
    if not fruits:
        print("\nThere are no fruits")
    else:
        for fruit, datos in fruits.items():
            print(f"\nfruit: {fruit}")
            print(f"Characteristics: {datos["Characteristics"]}")
            print(f"Information: {datos["Information"]}")
            print()

def exit():
    print("Exit..")

options = {
    "1": addFruit,
    "2": editFruit,
    "3": deletedFruit,
    "4": printFruits,
    "5": exit
}

def menu():
    while True:
        print("\nWelcome of Menu!!")
        print("1. add fruit")
        print("2. edit fruit")
        print("3. deleted fruit")
        print("4. print fruits")
        print("5. exit")
        option = input("Enter the option:")

        function = options.get(option)

        if function:
            function()
            if option == "5":
                break
        else:
            print("\nThe option is invalid")
menu()