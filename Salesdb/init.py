import sqlite3 as s
conn=s.connect('SalesDB/sales.db')
cursor=conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               customer_name TEXT NOT NULL,
               product_name TEXT NOT NULL,
               quantity INTEGER NOT NULL,
               price REAL NOT NULL,
               sales_date DATE NOT NULL
               )
               ''')
cursor.execute(''' 
INSERT INTO sales(customer_name,product_name,quantity,price,sales_date)
               values
               ('ALice','Laptop',1,1200.00,'1013-01-15'),
               ('Bob','Mouse',2,25.00,'2023-01-16'),
               ('Charlie','KeyBoard',1,75.00,'2023-01-17'),
               ('Eve','Laptop',1,1200.00,'2023-01-21'),
               ('Frank','Mouse',3,25.00,'2023-01-21')
            ''')
conn.commit()
conn.close()