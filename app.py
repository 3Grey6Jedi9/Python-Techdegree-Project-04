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
        session.commit()
        return inventory






def menu():
    while True:
        print("""
        \n           MAIN MENU\n
        \r1) View details [press 'V']
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





def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == 'V':
            pass
        elif choice == 'A':
            pass
        elif choice == 'B':
            pass
        else:
            print('GOODBYE SWEETHEART')
            app_running = False



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()
    #add_csv()

    #for p in session.query(Product):
        #print(p)









