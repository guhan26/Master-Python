
-- Select Statement is used to view table
SELECT * FROM students.employee;
SELECT EmpID,EmpName FROM students.employee;

-- Distinct is keywoord used to return distinct(Unirue) values
SELECT distinct EmpDept FROM students.employee;

-- The COUNT is returning the number of rows in the table
SELECT count(EmpDept) FROM students.employee;

-- The WHERE clause is used to filter records
SELECT * FROM students.employee
WHERE EmpName = 'Guhan';
WHERE EmpAge < 25;
