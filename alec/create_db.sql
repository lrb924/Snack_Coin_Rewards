BEGIN;

CREATE TABLE IF NOT EXISTS Menus (
    id INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Food (
    id INTEGER PRIMARY KEY,
    name TEXT,
    about TEXT,
    category TEXT,
    picture TEXT,
    unitprice FLOAT
);

CREATE TABLE IF NOT EXISTS MenuItems (
    menu_id INTEGER,
    food_id INTEGER,
    FOREIGN KEY (menu_id) REFERENCES Menus(id),
    FOREIGN KEY (food_id) REFERENCES Food(id)
);

CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    phone INTEGER,
    email TEXT
);

CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total FLOAT,
    time DATETIME,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

CREATE TABLE IF NOT EXISTS OrderItems (
    order_id INTEGER,
    menu_id INTEGER,
    quantity INTEGER,
    price FLOAT,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (menu_id) REFERENCES Menus(id)
);

CREATE TABLE IF NOT EXISTS Rewards (
    customer_id INTEGER,
    snak_tokens FLOAT,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

END;