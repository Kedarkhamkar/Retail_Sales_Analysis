# configuration
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    password="Kedar@2506",
    database="retail_sale_db",
    use_pure=True
)

cur = con.cursor()

print("MySQL connected successfully!")

# data manipulation functions

def add_sale():
    product = input("Enter Product Name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    sale_date = input("Enter Sale Date (YYYY-MM-DD): ")

    query = """
    insert into Sales(product_name, category, quantity, price, sale_date)
    values (%s, %s, %s, %s, %s)
    """  

    values = (product, category, quantity, price, sale_date)

    cur.execute(query, values)
    con.commit()
 
# call the function for execution   
#add_sale()

def view_sale():
    cur.execute("select*from sales")
    
    records = cur.fetchall()
    
    print("\nsales record")
    
    for row in records:
        print(row)
    
# view_sale()

def update_sale():
    query = "update sale set quantity = %s where sale_id = %s "
    
    values = (
        23,2
    )
    
    cur.execute(query,values)
    con.commit()
    
    #delete sale
    #total revenue
    
while True:
    print("--------------")
    print("retail sale data")
    print("--------------")
    
    
    print("1.add sale")
    print("2.view sale")
    print("3.update sale")
    print("4.exit")
    
    option = int(input("enter an option 1/2/3/4 only : "))
    
    if(option == 1):
        add_sale()
    elif(option == 2):
        view_sale()
    elif(option == 3):
        update_sale()
    elif(option == 4):
        print("Thank you")
        break
    else:
        print("invalid option.")
        
    con.close()            