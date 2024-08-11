-- Temporal
SELECT * FROM students.employee;
SELECT current_time()

-- String Functions and Operation
SELECT  LENGTH(EmpName) FROM students.employee;
SELECT employee.EmpName || employee.EmpLastName AS FULLLNAME
FROM students.employee;

-- In SQL a Subquery can be simply defined as a query within another query
SELECT EMPID,EmpName
FROM students.employee
WHERE EmpAge >
(SELECT AVG(EmpAge) FROM students.employee);

-- A self join is a regular join, but the table is joined with itself
SELECT EmpID,students.student.Std_id,employee.EmpAge,student.Std_Age
FROM students.student
INNER JOIN students.employee
ON students.student.Std_id = students.employee.EmpID;
