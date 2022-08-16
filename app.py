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
                session.add(new_product)
        session.commit()






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
    # add_csv()

    for p in session.query(Product):
        print(p)

    a = session.query(Product).filter_by(product_name='Apple - Granny Smith').count()
    print(a)

# Estoy añadiendo cada vez mas datos a los que hay quizas tenga que elminar y volver a crear la base de datos
# ver como puedo evitar eso y dejarlo bien








