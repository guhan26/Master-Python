
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

-- The ORDER BY keyword is used to sort the result-set in ascending or descending order(end of the query)
SELECT * FROM students.employee
ORDER BY EmpAge ASC;
ORDER BY EmpAge DESC;

-- The LIMIT clause is used to specify the number of records to return
SELECT * FROM students.employee
ORDER BY EmpAge ASC
LIMIT 3;

-- The BETWEEN operator selects values within a given range
SELECT * FROM students.employee
WHERE EmpAge BETWEEN  24 AND 26;

-- The IN operator allows you to specify multiple values in a WHERE clause
SELECT * FROM students.employee
WHERE EmpAge IN (23,25,29)
ORDER BY EmpAge ASC ; 

-- The LIKE operator is used in a WHERE clause to search for a specified pattern in a column
SELECT * FROM students.employee
WHERE EmpName LIKE 'K%';
WHERE EmpName LIKE '%n%';
WHERE EmpName LIKE '_a%';

