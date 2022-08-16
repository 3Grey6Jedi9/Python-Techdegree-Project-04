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










