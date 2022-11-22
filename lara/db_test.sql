BEGIN;


select * from Menus;

select * from Food;

select * from MenuItems;


insert into Customers (first_name, last_name, phone, email)
values
        ("Joe", "Shmoe", "5554443333", "joeshmoe@email.com");

select * from Customers;


insert into Orders (customer_id, time)
values
        (1, datetime('now'));

select * from Orders;

SELECT order_total FROM Orders WHERE id = 16

SELECT id FROM Orders ORDER BY id DESC LIMIT 1 OFFSET 0

SELECT order_total FROM Orders WHERE id = 27

delete from Orders
where id >0;

insert into OrderItems (order_id, menu_id, food_id, quantity, item_total)
values
        (1, 1, 2, 2, 0.012);

select * from OrderItems;


insert into Rewards (customer_id, order_id, snak_tokens)
values
        (1, 1, 12.0);

select * from Rewards;

/* Link Food & Menu */
select * from Food
where id in (
    select food_id from MenuItems
    where menu_id = 1);


END;