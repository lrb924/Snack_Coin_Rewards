/* Creates snack.db table structure */

BEGIN;

DROP TABLE IF EXISTS Menus;
CREATE TABLE IF NOT EXISTS Menus (
    id INTEGER PRIMARY KEY
);

DROP TABLE IF EXISTS Food;
CREATE TABLE IF NOT EXISTS Food (
    id INTEGER PRIMARY KEY,
    name TEXT,
    about TEXT,
    category TEXT,
    image TEXT,
    unit_price FLOAT
);

DROP TABLE IF EXISTS MenuItems;
CREATE TABLE IF NOT EXISTS MenuItems (
    menu_id INTEGER,
    food_id INTEGER,
    FOREIGN KEY (menu_id) REFERENCES Menus(id),
    FOREIGN KEY (food_id) REFERENCES Food(id)
);

DROP TABLE IF EXISTS Customers;
CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER PRIMARY KEY,
    wallet TEXT,
    first_name TEXT,
    last_name TEXT,
    phone INTEGER,
    email TEXT
);

DROP TABLE IF EXISTS Orders;
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_total FLOAT,
    time DATETIME,
    completed BOOLEAN,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

DROP TABLE IF EXISTS OrderItems;
CREATE TABLE IF NOT EXISTS OrderItems (
    order_id INTEGER,
    food_id INTEGER,
    menu_id INTEGER,
    quantity INTEGER,
    item_total FLOAT,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (food_id) REFERENCES Food(id),
    FOREIGN KEY (menu_id) REFERENCES Menus(id)
);

DROP TABLE IF EXISTS Rewards;
CREATE TABLE IF NOT EXISTS Rewards (
    customer_id INTEGER,
    order_id INTEGER,
    snak_tokens FLOAT,
    FOREIGN KEY (customer_id) REFERENCES Customers(id),
    FOREIGN KEY (order_id) REFERENCES Orders(id)
);

END;