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

select * from OrderItems;

select * from Orders;

select * from Rewards;

END;