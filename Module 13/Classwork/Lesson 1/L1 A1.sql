create table supplier (
    SNO text primary key,
    SNAME text,
    STATUS integer,
    CITY text
);

insert into supplier (SNO, SNAME, STATUS, CITY) values
    ('S1', 'Smith', 20, 'London'),
    ('S2', 'Jones', 10, 'Paris'),
    ('S3', 'Blake', 30, 'Paris'),
    ('S4', 'Clark', 20, 'London'),
    ('S5', 'Adams', 30, 'Athens');

select * from supplier;