create table restaurant (
    order_no char(4) primary key,
    order_date text,
    customer_name text,
    item_name text,
    quantity int,
    price real
);

insert into restaurant (order_no, order_date, customer_name, item_name, quantity, price) values
    ('0001', '2024-06-01', 'Alice', 'Burger', 2, 5.99),
    ('0002', '2024-06-01', 'Bob', 'Pizza', 1, 8.99),
    ('0003', '2024-06-02', 'Charlie', 'Salad', 3, 4.50),
    ('0004', '2024-06-02', 'Diana', 'Pasta', 1, 7.25),
    ('0005', '2024-06-03', 'Ethan', 'Soda', 4, 1.50);

select * from restaurant;

select * from restaurant
where quantity = 1;