from models import Base, session, Product, engine
import datetime
import csv

def add_csv():
    inventory = []
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            if len(row[2]) < 3:
                dict = {'Name': row[0], 'Price':clean_price(row[1]), 'Quantity': clean_quantity(row[2]), 'Date': clean_date(row[3])}
                inventory.append(dict)
                new_product = Product(product_name=dict['Name'], product_price=dict['Price'],
                                      product_quantity=dict['Quantity'],
                                      date_update=dict['Date'])
                if new_product not in session.query(Product):
                    session.add(new_product)
                else:
                    session.query(Product).filter_by(product_name=new_product.product_name).delete()
                    session.add(new_product)
        session.commit()
        return inventory






def menu():
    while True:
        print("""
        \n           MAIN MENU\n
        \r1) View products details [press 'V']
        \r2) Add product in the database [press 'A']
        \r3) Make a backup [press 'B']
        \r4) Exit [press 'E']
        """)
        choice = input('What would you like to do? ').upper()
        if choice in ['V', 'A','B','E']:
            return choice
        else:
            input(''' \nPlease choose one of the options above.
            \r['V', 'A','B','E']
            \rPress enter to try again.''')

def clean_quantity(quantstr):
    quantity = int(quantstr)
    return quantity

def clean_price(pricestr):
    pricels = pricestr.split('$')
    price = int(float(pricels[1])*100)
    return price


def clean_date(datestr):
    date = datetime.datetime.strptime(datestr, '%m/%d/%Y')
    return date


def inventory_updated(inventoryapp):
    inventory0 = add_csv()
    if inventoryapp != inventory0:
        inventory = inventoryapp
    else:
        inventory = inventory0
    return inventory

def backup(inv):
    inventory = inventory_updated(inv)
    with open('inventory_backup.csv', 'a') as csvbackup:
        fieldnames = ['Name', 'Price', 'Quantity', 'Date']
        backupwriter = csv.DictWriter(csvbackup, fieldnames=fieldnames)

        backupwriter.writeheader()

        for item in inventory:
            backupwriter.writerow({'Name': item['Name'], 'Price': item['Price'], 'Quantity': item['Quantity'], 'Date': item['Date']})












def app():
    inventory = add_csv()
    app_running = True
    while app_running:
        choice = menu()
        if choice == 'V':
            for product in inventory:
                print(f'''{inventory.index(product)+1} <-- {product['Name']} --> {inventory.index(product)+1}''')
            while ValueError:
                try:
                    p = int(input('\nEnter the product id number in order to know more about it: '))
                    if p not in range(1,len(inventory)):
                        raise ValueError('\nPlease select an available id')
                except ValueError as err:
                    print('{}'.format(err))
                else:
                    print(f'''\n{inventory[p - 1]}''')
                    break
        elif choice == 'A':
            message = input("You have selected adding a new product...Press Enter to proceed")
            name = input("Please enter the product's name: ")
            price = clean_price(input("Please enter the product's price[for example:$9.99]:"))
            quantity = clean_quantity(input("Now I'll need you to tell me the quantity: "))
            date = datetime.datetime.now()
            new_product = Product(product_name=name, product_price=price, product_quantity=quantity, date_update=date)
            if new_product not in session.query(Product):
                session.add(new_product)
                dict = dict = {'Name': new_product.product_name, 'Price': new_product.product_price, 'Quantity': new_product.product_quantity, 'Date': new_product.date_update}
                inventory.append(dict)
                inventory_updated(inventory)
        elif choice == 'B':
            backup(inventory)
        else:
            print('GOODBYE SWEETHEART')
            app_running = False









if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()
    #add_csv()

   # for p in session.query(Product):
    #    print(p)










