CREATE TABLE IF NOT EXISTS Employees (
    Employee_ID INT PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INT
);

INSERT INTO Employees (Employee_ID, Name, Department, Salary) VALUES
(1, 'John Doe', 'Sales', 60000),
(2, 'Jane Smith', 'Marketing', 75000),
(3, 'Emily Davis', 'IT', 90000),
(4, 'Michael Brown', 'HR', 65000),
(5, 'Jessica Wilson', 'Finance', 80000),
(6, 'Daniel Garcia', 'IT', 95000),
(7, 'Sarah Martinez', 'Sales', 62000),
(8, 'David Anderson', 'Marketing', 72000),
(9, 'Laura Thomas', 'Finance', 85000),
(10, 'James Taylor', 'HR', 68000);

SELECT * FROM Employees;

SELECT SUM(Salary) AS Total_Salary FROM Employees;

SELECT AVG(SALARY) AS Average_Salary FROM Employees;

SELECT COUNT(DISTINCT Department) AS No_of_Departments FROM Employees;

SELECT MIN(Salary) AS Minimum_Salary FROM Employees;

SELECT MAX(Salary) AS Maximum_Salary FROM Employees;