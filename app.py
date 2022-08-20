from models import Base, session, Product, engine
import datetime
import csv


def add_csv():
    inventory = []
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            if len(row[2]) < 4:
                dict = {'Name': row[0], 'Price':clean_price(row[1]), 'Quantity': clean_quantity(row[2]), 'Date': clean_date(row[3])}
                new_product = Product(product_name=dict['Name'], product_price=dict['Price'],
                                      product_quantity=dict['Quantity'],
                                      date_update=dict['Date'])
                if session.query(Product).count() >= 27:
                    L = []
                    for p in session.query(Product.product_name):
                        L.append(p.product_name)
                    if f'{new_product.product_name}' not in L:
                        session.add(new_product)
                        inventory.append(dict)
                    else:
                        for p in session.query(Product):
                            a = str(p).split(';')
                            name = str(a[0]).split(':')
                            if name[1] == f' {new_product.product_name}':
                                p.product_price = new_product.product_price
                                p.product_quantity = new_product.product_quantity
                                p.date_update = new_product.date_update
                            else:
                                continue
                if session.query(Product).count() < 27:
                    session.add(new_product)
                    inventory.append(dict)
        session.commit()
        products = session.query(Product)
        return products








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



def print_date(datestrp):
    if list(datetime.datetime.strftime(datestrp, '%d'))[1] == '1' and list(datetime.datetime.strftime(datestrp, '%d'))[0] != '1':
        date = datetime.datetime.strftime(datestrp, '%B %dst of %Y')
    elif list(datetime.datetime.strftime(datestrp, '%d'))[1] == '2' and list(datetime.datetime.strftime(datestrp, '%d'))[0] != '1':
        date = datetime.datetime.strftime(datestrp, '%B %dsd of %Y')
    elif list(datetime.datetime.strftime(datestrp, '%d'))[1] == '3' and list(datetime.datetime.strftime(datestrp, '%d'))[0] != '1':
        date = datetime.datetime.strftime(datestrp, '%B %dsd of %Y')
    else:
        date = datetime.datetime.strftime(datestrp, '%B %dth of %Y')
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



def print_nice(a):
    b = str(a)
    c = b.split(';')
    d = str(c[2])
    e = d.split(':')
    f = str(c[3]).split(':')
    print(f[1])
    dt = datetime.datetime.strptime(f[1],' %Y-%m-%d')
    print(f'''\n {c[0]}
    \n{c[1]}
    \n Price: ${int(e[1])/100}
    \n Updated: {datetime.datetime.strftime(dt,'%B %d %Y')}''')
# Put days more fancy

def print_date_nice(datep):
    d = datetime.datetime.strftime(datep,'%d')
    if d == '01' or d == '21' or d == '31':
        return datetime.datetime.strftime(datep, '%B %dst of %Y')
    if d == '02' or d == '22':
        return datetime.datetime.strftime(datep, '%B %dnd of %Y')
    if d == '03' or d == '23':
        return datetime.datetime.strftime(datep, '%B %drd of %Y')
    else:
        return datetime.datetime.strftime(datep, '%B %dth of %Y')









def app():
    products = add_csv()
    app_running = True
    while app_running:
        choice = menu()
        if choice == 'V':
            id = 1
            for product in session.query(Product.product_name):
                print(f'{id}   {product.product_name}')
                id += 1
            while ValueError:
                try:
                    p = int(input('\nEnter the product id number in order to know more about it: '))
                    if p not in range(1,session.query(Product).count()+1):
                        raise ValueError('\nPlease select an available id')
                except ValueError as err:
                    print('{}'.format(err))
                else:
                    for q in session.query(Product.product_id):
                        if p == q.product_id:
                           j = 1
                           for a in session.query(Product):
                               if p == j:
                                   print_nice(a)
                               else:
                                   j += 1
                                   continue
                    break
        elif choice == 'A':
            message = input("You have selected adding a new product...Press Enter to proceed")
            name = input("Please enter the product's name: ")
            while IndexError:
                try:
                    price = clean_price(input('Please enter the price using this format[$9.99]:'))
                except IndexError:
                    print('Use the given format please')
                else:
                    break
            while ValueError:
                try:
                    quantity = int(input('Now tell my the quantity if you are so kind: '))
                except ValueError:
                    print('You must enter an integer please')
                else:
                    break
            new_date = datetime.datetime.now()
            updatedstr = datetime.datetime.strftime(new_date, '%m/%d/%Y')
            updated = clean_date(updatedstr)
            updated_nice = print_date_nice(updated)
            new_product = Product(product_name=name , product_price=price , product_quantity=clean_quantity(quantity), date_update=updated)
            L = []
            for p in session.query(Product.product_name):
                L.append(p.product_name)
            if f'{new_product.product_name}' not in L:
                session.add(new_product)
            else:
                for p in session.query(Product):
                    a = str(p).split(';')
                    name = str(a[0]).split(':')
                    if name[1] == f' {new_product.product_name}':
                        p.product_price = new_product.product_price
                        p.product_quantity = new_product.product_quantity
                        p.date_update = new_product.date_update
                    else:
                        continue
            session.commit()
        elif choice == 'B':
            backup(inventory)
            print(inventory)
        else:
            print('GOODBYE SWEETHEART')
            app_running = False
    print(inventory)



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()
    #add_csv()

    #for p in session.query(Product):
        #print(p)

# Mirar de nuevo SQLAlchemy y crear la aplicación correctamente

# Poner la base de datos en el mismo formato

    #for p in session.query(Product):
        #a = str(p).split(';')
        #name = str(a[0]).split(':')
        #print(name[1])


    #product01 = Product(product_name='Tom', product_price='$4.44',
            #product_quantity=34,
            #date_update=datetime.datetime.now())
    #print(f' {product01.product_name}')
    #product02 = Product(product_name='Tom', product_price=990,
            #product_quantity=dict['Quantity'],
            #date_update=dict['Date'])

    #if product01.product_name == product02.product_name:
        #print('True')
    #else:
        #print('False')

    #a = Product.product_name=product02.product_name
    #print(a)

    #for p in session.query(Product):
        #if p != product02:
            #print(False)
        #else:
            #continue


   # Solucionar duplicados en la creación de la base de datos. Si el producto ya exite no se añade solo si no estaba

   # Fix the app() function


    #for p in session.query(Product):
        #a = str(p).split(';')
        #name = str(a[0]).split(':')
        #b = f' {new_product.product_name}'
        #c = name[1]
        #if b == c:
            #print('I found it')
        #else:
            #continue



    #for p in session.query(Product):
        #p.product_name = 'Tom'
        #print(p)

    #L = []
    #for p in session.query(Product.product_name):
        #L.append(p.product_name)
    #print(L)

    #if 'Radish' in L:
        #print(True)












