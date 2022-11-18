BEGIN;


/*
delete from food
where id > 6;
*/

select * from Menus;

select * from Food;

select * from MenuItems;


insert into Customers (first_name, last_name, phone, email)
values
        ("Joe", "Shmoe", "5554443333", "joe.shmoe@email.com");

select * from Customers;

insert into Orders (customer_id, order_total, time)
values
        (1, 0.012, datetime('now'));

select * from Orders;


insert into OrderItems (order_id, menu_id, food_id, quantity, item_total)
values
        (1, 1, 2, 2, 0.012);

select * from OrderItems;

delete from Rewards
where customer_id = 1;


insert into Rewards (customer_id, order_id, snak_tokens)
values
        (1, 1, 0.12);

select * from Rewards;


END;