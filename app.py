from models import Base, session, Product, engine
import datetime
import csv

def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)

def menu():
    while True:
        print("""
        \nPRODUCTS
        \r1) Add product
        \r2) View all
        \r3) Search for product
        \r4) Product Analysis 
        \r5) Exit
        """)
        choice = input('What would you like to do? ')
        if choice in ['1','2','3','4','5']:
            return choice
        else:
            input(''' \nPlease choose one of the options above.
            \rA number from 1-5.
            \rPress enter to try again.''')

def clean_quantity(quantstr):
    quantity = int(quantstr)
    return quantity

def clean_price(pricestr):
    L = []
    i = 0
    for b in pricestr:
        if i > 0:
            L.append(b)
            i = 1
        else:
            i = 1
            continue
    L.pop(1)

    price = L[0] + L[1] + L[2]

    return int(price)




def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            print('GOODBYE')
            app_running = False



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # app()
    add_csv()










