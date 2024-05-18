import sqlite3
conn = sqlite3.connect('retail_store.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE Customers (
        CustomerID INTEGER PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        Email TEXT,
        DateOfBirth TEXT
    )
''')
cursor.execute('''
    CREATE TABLE Products (
        ProductID INTEGER PRIMARY KEY,
        ProductName TEXT,
        Price REAL
    )
''')
cursor.execute('''
    CREATE TABLE Orders (
        OrderID INTEGER PRIMARY KEY,
        CustomerID INTEGER,
        OrderDate TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    )
''')
cursor.execute('''
    CREATE TABLE OrderItems (
        OrderItemID INTEGER PRIMARY KEY,
        OrderID INTEGER,
        ProductID INTEGER,
        Quantity INTEGER,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    )
''')
customers = [
    (1, 'John', 'Doe', 'john.doe@example.com', '1985-01-15'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com', '1990-06-20')
]
cursor.executemany('INSERT INTO Customers VALUES (?, ?, ?, ?, ?)', customers)
products = [
    (1, 'Laptop', 1000),
    (2, 'Smartphone', 600),
    (3, 'Headphones', 100)
]
cursor.executemany('INSERT INTO Products VALUES (?, ?, ?)', products)

orders = [
    (1, 1, '2023-01-10'),
    (2, 2, '2023-01-12')
]
cursor.executemany('INSERT INTO Orders VALUES (?, ?, ?)', orders)
order_items = [
    (1, 1, 1, 1),
    (2, 1, 3, 2),
    (3, 2, 2, 1),
    (4, 2, 3, 1)
]
cursor.executemany('INSERT INTO OrderItems VALUES (?, ?, ?, ?)', order_items)

conn.commit()
conn.close()
import sqlite3
conn = sqlite3.connect('retail_store.db')
cursor = conn.cursor()
print("1. List all customers")
cursor.execute('SELECT * FROM Customers')
for row in cursor.fetchall():
    print(row)
print("\n2. Find all orders placed in January 2023")
cursor.execute('SELECT * FROM Orders WHERE OrderDate LIKE "2023-01%"')
for row in cursor.fetchall():
    print(row)

print("\n3. Get the details of each order, including the customer name and email")
cursor.execute('''
    SELECT Orders.OrderID, Customers.FirstName, Customers.LastName, Customers.Email, Orders.OrderDate
    FROM Orders
    JOIN Customers ON Orders.CustomerID = Customers.CustomerID
''')
for row in cursor.fetchall():
    print(row)

print("\n4. List the products purchased in a specific order (OrderID = 1)")
cursor.execute('''
    SELECT Products.ProductName, OrderItems.Quantity
    FROM OrderItems
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    WHERE OrderItems.OrderID = 1
''')
for row in cursor.fetchall():
    print(row)
print("\n5. Calculate the total amount spent by each customer")
cursor.execute('''
    SELECT Customers.FirstName, Customers.LastName, SUM(Products.Price * OrderItems.Quantity) AS TotalSpent
    FROM Orders
    JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    GROUP BY Customers.CustomerID
''')
for row in cursor.fetchall():
    print(row)

print("\n6. Find the most popular product")
cursor.execute('''
    SELECT Products.ProductName, SUM(OrderItems.Quantity) AS TotalOrdered
    FROM OrderItems
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    GROUP BY Products.ProductID
    ORDER BY TotalOrdered DESC
    LIMIT 1
''')
for row in cursor.fetchall():
    print(row)

print("\n7. Get the total number of orders and the total sales amount for each month in 2023")
cursor.execute('''
    SELECT strftime('%Y-%m', Orders.OrderDate) AS Month, COUNT(DISTINCT Orders.OrderID) AS TotalOrders, SUM(Products.Price * OrderItems.Quantity) AS TotalSales
    FROM Orders
    JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    WHERE strftime('%Y', Orders.OrderDate) = '2023'
    GROUP BY Month
''')
for row in cursor.fetchall():
    print(row)

print("\n8. Find customers who have spent more than $1000")
cursor.execute('''
    SELECT Customers.FirstName, Customers.LastName, SUM(Products.Price * OrderItems.Quantity) AS TotalSpent
    FROM Orders
    JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
    JOIN Products ON OrderItems.ProductID = Products.ProductID
    GROUP BY Customers.CustomerID
    HAVING TotalSpent > 1000
''')
for row in cursor.fetchall():
    print(row)
conn.close()
