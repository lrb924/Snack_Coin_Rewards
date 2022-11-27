/* Inserts menu data into snack.db */

BEGIN;

insert into Menus (id)
values
        (1);

insert into Food (name, about, category, image, unit_price)
values
        ("Hotdog", "Chicago style, no ketchup", "Entree", "./Images/hotdog.jpeg", 0.004),
        ("Pizza", "Cheese, one slice", "Entree", "./Images/pizza.jpeg", 0.006),
        ("Fries", "Salty!", "Side", "./Images/fries.jpeg", 0.002),
        ("Milkshake", "Chocolate & Vanilla", "Drink", "./Images/milkshake.jpg", 0.005),
        ("Cake", "Chocolate ganache", "Dessert", "./Images/ganache_cake.jpg", 0.003);

insert into MenuItems (menu_id, food_id)
values
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6);

END;