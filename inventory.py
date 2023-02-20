# The library tabulate is imported. 
from tabulate import tabulate

# The class "Shoe" stores attributes of country, code, product, cost and quantity.  Various methods 
# are also stored here in relation to these attributes, which return these attributes as well as 
# formatting.
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code 
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)
    
    def get_code(self):
        return self.code

    def get_product(self):
        return self.product
    
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity 
    
    def get_list(self):
        return [self.country, self.code, self.product, str(self.cost), str(self.quantity)]

    def set_quantity(self, new_quantity):
        self.quantity = int(new_quantity)

    def __str__(self):
        return f"""
Country of origin:  {self.country}
Product Code:       {self.code}
Product Name:       {self.product}
Shoe cost:          {self.cost}
Quantity:           {self.quantity}    
"""
#==========Functions outside the class==============
shoe_list = []

# The file inventory.txt is read and the contents added to the list.
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            next(file)
            for line in file:
                line = line.split(',')
                shoe_list.append(Shoe(line[0], line[1], line[2], line[3], line[4]))
    # The program quits if the file is not located.
    except FileNotFoundError:
        print("\nThe program is unable to run at this time. We apologise for the inconvenience. Goodbye.")
        exit()

# The user inputs new shoe details, which is added to shoe_list. 
def capture_shoes():
    print("You will be asked details about the show below.")
    # The user is asked to re-enter if an empty string is entered.
    while True:
        country_input = input("What is the country of origin of the product?: ")
        if country_input == "":
            print("Please enter a country.")
            continue
        else:
            break
    # The user is asked to re-enter if the code is not unique or in the format set out.
    while True:
        code_input = input("Enter the product code, in the format SKU#####: ")
        if len(code_input) != 8 or code_input[0:3] != "SKU":
            print("Please enter a valid code.")
            continue
        else:
            if not code_input[3:].isnumeric():
                print("Please enter a valid code.")
                continue 
            else:
                for shoe in shoe_list:
                    if shoe.get_code() == code_input:
                        print("This code already exist. Please enter an unique code for the product.")
                        break
                else:
                    break
    # The user is asked to re-enter if an empty string is returned.
    while True:
        product_input = input("Enter the product name: ")
        if product_input == "":
            print("Please enter a name.")
            continue
        else:
            break
    # The input must be a float variable.
    while True:
        try:
            cost_input = float(input("What is the cost per shoe in R?: "))
            break
        except:
            print("Please enter a valid number for the cost.")
    # The input must be an integer variable.
    while True:
        try:
            quantity_input = int(input("What is the quantity available?: "))
            break
        except:
            print("Please enter a valid integer.")
    # All inputs added to a new Shoe object, which is added to list and written to file.
    shoe_list.append(Shoe(country_input, code_input, product_input, cost_input, quantity_input))
    with open('inventory.txt', 'w') as file:
        file.write(f"Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(','.join(shoe.get_list()) + "\n")
    print("\nYour data has been added!\n")

# The contents of the file is printed in table format. 
def view_all():
    table = []
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    for shoe in shoe_list:
        table.append(shoe.get_list())
    print("\n" + tabulate(table, headers, tablefmt='simple_grid')) 
    
# The shoe with lowest quantity is brought up, and the user is asked to input a new restock amount.  
# The updated list overwrites current file contents.
def re_stock():
    min_quantity = shoe_list[0]
    for shoe in shoe_list: 
        if min_quantity.get_quantity() > shoe.get_quantity():
            min_quantity = shoe
    quantity_update = input(f"\nThere are {min_quantity.get_quantity()} pairs left of {min_quantity.get_product()}. Would you like to update this quantity? y/n: ").lower()
    if quantity_update == "y":
        while True:
            try:
                quantity_update = int(input("\nPlease enter the new quantity of the product here: "))
                if quantity_update < min_quantity.get_quantity():
                    print("\nPlease enter a quantity higher than the current amount.")
                else:
                    break
            except:
                print("Please enter a valid number.")
        min_quantity.set_quantity(quantity_update)
        with open('inventory.txt', 'w') as file:
            file.write(f"Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(','.join(shoe.get_list()) + "\n")
        print("The details have been updated.")
    else:
        print("\nYou will be brought back to the main menu.")

# The user inputs a shoe code, and details of the relevant shoe is printed. 
def search_shoe():
    shoe_search = input("\nPlease enter the shoe code here: ")
    for shoe in shoe_list:
        if shoe_search == shoe.get_code():
            print(f"\nHere are your shoe details:\n{shoe}")
            return 
    print("\nCode not recognised. You will be taken back to the main menu now.")

# The total value for each shoe is printed.  
def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_quantity() * shoe.get_cost()
        print(f"\nThe value of {shoe.get_product()} is R{value:.2f}.")

# The shoe with the highest quantity in the file is printed and advertised
# as being on sale. 
def highest_qty():
    highest_quantity = shoe_list[0]
    for shoe in shoe_list: 
        if highest_quantity.get_quantity() < shoe.get_quantity():
            highest_quantity = shoe
    print(f"\nThe product {highest_quantity.get_product()} is for sale.")


read_shoes_data()
print("It's shoe time!")
while True:
    # The user inputs a selection relative to the menu options.  Each option recalls a function 
    # above. 
    menu = input(f"""\nPlease select an option from the menu below.
1 - Add New Shoe 
2 - View All Shoes
3 - Restock
4 - Search For A Shoe
5 - Value of Each Shoe
6 - Shoe for Sale
7 - Quit\n""")
    if menu == "1":
        capture_shoes()
    elif menu == "2":
        view_all() 
    elif menu == "3":
        re_stock() 
    elif menu == "4":
        search_shoe()
    elif menu == "5":
        value_per_item()
    elif menu == "6":
        highest_qty()
    # The user exits the program.
    elif menu == "7":
        print("Thank you for using our services today. We bid you farewell.")
        exit()
    # The user is prompted to try again if the input is not recognised. 
    else:
        print("Your input was not recognised. Please try again!")