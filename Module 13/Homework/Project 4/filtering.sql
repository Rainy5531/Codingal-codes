CREATE TABLE IF NOT EXISTS Students (
    Admission_ID VARCHAR(6) PRIMARY KEY,
    Name VARCHAR(50),
    Grade INT,
    Marks_Percentage INT
);

INSERT INTO Students (Admission_ID, Name, Grade, Marks_Percentage) VALUES
(000001, 'Alice Johnson', 10, 85),
(000002, 'Bob Smith', 11, 92),
(000003, 'Charlie Brown', 10, 78),
(000004, 'Diana Prince', 12, 88),
(000005, 'Ethan Hunt', 11, 95),
(000006, 'Fiona Glenanne', 10, 80),
(000007, 'George Clooney', 12, 91),
(000008, 'Hannah Montana', 11, 87),
(000009, 'Ian Somerhalder', 10, 93),
(000010, 'Jenna Fischer', 12, 76);

SELECT * FROM Students;

SELECT * FROM Students
WHERE Grade = 10 AND Marks_Percentage < 90;

SELECT * FROM Students
WHERE Grade = 10 AND Marks_Percentage >= 90;

SELECT * FROM Students
WHERE Marks_Percentage BETWEEN 80 AND 90;

SELECT * FROM Students
WHERE Grade IN (10, 12);

SELECT * FROM Students
WHERE Grade NOT IN (11);

SELECT * FROM Students
WHERE Marks_Percentage < 80;

SELECT * FROM Students
WHERE Name LIKE 'A%';

SELECT * FROM Students
WHERE Name LIKE '%n';

SELECT * FROM Students
WHERE Name LIKE '%o%'AND Grade = 11;