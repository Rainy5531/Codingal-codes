create table if not exists Salesman (
    Salesman_id text primary key,
    name text,
    city text,
    commission real
);

insert into Salesman (Salesman_id, name, city, commission) values
    ('5001', 'James Hoog', 'New York', 0.15),
    ('5002', 'Nail Knite', 'Paris', 0.13),
    ('5005', 'Pit Alex', 'London', 0.11),
    ('5006', 'Mc Lyon', 'Paris', 0.14),
    ('5007', 'Paul Adam', 'Rome', 0.13),
    ('5003', 'Lauson Hen', 'San Jose', 0.12);

select * from Salesman;

select * from Salesman
where city = 'Paris';

select name, commission
from Salesman;

create table if not exists Orders (
    ord_no text primary key,
    purch_amt real,
    ord_date text,
    customer_id text,
    salesman_id text
); 

insert into Orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) values
    ('70001', 150.5, '2012-10-05', '3005', '5002'),
    ('70009', 270.65, '2012-09-10', '3001', '5001'),
    ('70002', 65.26, '2012-10-05', '3002', '5003'),
    ('70004', 110.5, '2012-08-17', '3009', '5007'),
    ('70007', 948.5, '2012-09-10', '3005', '5002');
    
select * from Orders;