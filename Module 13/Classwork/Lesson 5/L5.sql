-- Create the Salesman table if it doesn't exist
CREATE TABLE IF NOT EXISTS Salesman (
    salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    commission REAL
);

-- Insert sample data into the Salesman table
INSERT INTO Salesman (salesman_id, name, city, commission) VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5002', 'Nail Knite', 'Paris', 0.13),
('5005', 'Pit Alex', 'London', 0.11),
('5006', 'Mc Lyon', 'San Jose', 0.14),
('5007', 'Paul Adam', 'Rome', 0.13),
('5003', 'Lauson Hen', 'San Jose', 0.12);

-- Create the Customer table if it doesn't exist
CREATE TABLE IF NOT EXISTS Customer (
    customer_id TEXT,
    cust_name TEXT PRIMARY KEY,
    city TEXT,
    grade INTEGER,
    salesman_id TEXT,
    FOREIGN KEY (salesman_id) REFERENCES Salesman(salesman_id)
);

-- Insert sample data into the Customer table
INSERT INTO Customer (customer_id, cust_name, city, grade, salesman_id) VALUES
('3002', 'nick rimando', 'New York', 100, '5001'),
('3007', 'brad davis', 'New York', 200, '5001'),
('3005', 'graham zusi', 'California', 200, '5002'),
('3008', 'julian green', 'London', 300, '5004'),
('3004', 'fabian johnson', 'Paris', 300, '5002'),
('3009', 'geoff cameron', 'Berlin', 100, '5003'),
('3003', 'jozy altidor', 'Moscow', 200, '5007'),
('3001', 'brad guzan', 'London', NULL, '5005');

-- Create the Ordes table if it doesn't exist
CREATE TABLE IF NOT EXISTS Orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (salesman_id) REFERENCES Salesman(salesman_id)
);

-- Insert sample data into the Ordes table
INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
('70001', 150.5, '2012-10-05', '3005', '5005'),
('70009', 270.65, '2012-09-10', '3001', '5001'),
('70002', 65.26, '2012-10-05', '3002', '5003'),
('70004', 110.5, '2012-08-17', '3009', '5007'),
('70007', 948.5, '2012-09-10', '3005', '5005'),
('70005', 2400.6, '2012-07-27', '3007', '5006');

-- Queries
SELECT * FROM Salesman;
SELECT * FROM Customer;
SELECT * FROM Orders;

-- Matchung customers and salesmen by city
SELECT Customer.cust_name, salesman.name, Customer.city
FROM Customer
JOIN Salesman ON Customer.city = Salesman.city;

-- Linking customers to their salesmen
SELECT Customer.cust_name, Salesman.name
FROM Customer
JOIN Salesman ON Customer.salesman_id = Salesman.salesman_id;

-- Fetching orders where customer's city doesn't match salesman's city
SELECT Orders.ord_no, Customer.cust_name, Orders.customer_id, Orders.salesman_id
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id
JOIN Salesman ON Orders.salesman_id = Salesman.salesman_id
WHERE Customer.city <> Salesman.city; -- '<>' = '!='

-- Fetching all orders with customer names
SELECT Orders.ord_no, Customer.cust_name
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id;

-- Customer with grades
SELECT Customer.cust_name AS "Customer", Customer.grade AS"Grade"
FROM Orders
JOIN Salesman ON Orders.salesman_id = Salesman.salesman_id
JOIN Customer ON Orders.customer_id = Customer.customer_id
WHERE Customer.grade IS NOT NULL;

-- Customers with salesmen where commission is between 0.12 and 0.14
SELECT Customer.cust_name AS "Customer",
Customer.city AS "City",
Salesman.name AS "Salesman",
Salesman.commission
FROM Customer
JOIN Salesman ON Customer.salesman_id = Salesman.salesman_id
WHERE Salesman.commission BETWEEN 0.12 AND 0.14;

-- Calculating commission for orders where customer grade as 200 or more
SELECT Orders.ord_no, Customer.cust_name, Salesman.commission AS "Commission%",
Orders.purch_amt * Salesman.commission AS "Commission"
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id
JOIN Salesman ON Orders.salesman_id = Salesman.salesman_id
WHERE Customer.grade >= 200;

-- Ordes on a specific date
SELECT *
FROM Customer
JOIN Orders ON Customer.customer_id = Orders.customer_id
Where Orders.ord_date = '2012-10-05';