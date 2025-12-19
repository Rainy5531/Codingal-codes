CREATE TABLE IF NOT EXISTS Customers (
    Customer_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Phone_No VARCHAR(10) UNIQUE,
    City VARCHAR(50),
    Grade_Value INT
);

INSERT INTO Customers (Customer_ID, Name, Phone_No, City, Grade_Value) VALUES
(1, 'Alice Johnson', '6728921234', 'New York', 98),
(2, 'Bob Smith', '5029025678', 'Los Angeles', 97),
(3, 'Charlie Brown', '5089298765', 'Chicago', 102),
(4, 'Diana Prince', '8887664321', 'Houston', 99),
(5, 'Ethan Hunt', '9386226789', 'New York', 101),
(6, 'Fiona Glenanne', '7821829876', 'Miami', 95),
(7, 'George Clooney', '8787373456', 'Los Angeles', 103),
(8, 'Hannah Montana', '9384946543', 'New York', 103),
(9, 'Ian Somerhalder', '9398497890', 'Chicago', 100),
(10, 'Jenna Fischer', '3847942109', 'New York', 96);

SELECT * FROM Customers;

SELECT * FROM Customers
WHERE City = 'New York' OR Grade_Value > 100;

SELECT * FROM Customers
WHERE City = 'New York' AND Grade_Value > 100;