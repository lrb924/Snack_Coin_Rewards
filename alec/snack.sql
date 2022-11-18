BEGIN;

CREATE TABLE IF NOT EXISTS Menus (
    id integer PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Food (
    id integer PRIMARY KEY,
    name varchar(255),
    about varchar(255),
    category varchar(255),
    picture varchar(255),
    unitprice float
);

CREATE TABLE IF NOT EXISTS MenuItems (
    menu_id integer,
    food_id iteger,
    FOREIGN KEY (menu_id) REFERENCES Menus(id),
    FOREIGN KEY (food_id) REFERENCES Food(id)
);

CREATE TABLE IF NOT EXISTS Customers (
    id integer PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    phone int(10),
    email varchar(255)
);

CREATE TABLE IF NOT EXISTS Orders (
    id integer PRIMARY KEY,
    customer_id integer,
    total float,
    time datetime,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

CREATE TABLE IF NOT EXISTS OrderItems (
    order_id integer,
    menu_id integer,
    quantity integer,
    price float,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (menu_id) REFERENCES Menus(id)
);

CREATE TABLE IF NOT EXISTS Rewards (
    customer_id integer,
    snak_tokens float,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

END;