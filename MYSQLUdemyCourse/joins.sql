
-- The AS command is used to rename a column or table with an alias
SELECT EmpAge AS EMP_ID
FROM students.employee;

-- A JOIN is used to combine rows from two or more tables, based on a related column between them
SELECT EmpID,students.student.Std_id,employee.EmpAge,student.Std_Age
FROM students.student
  
-- INNER , LEFT , FULL JOIN
RIGHT JOIN students.employee
ON students.student.Std_id = students.employee.EmpAge;
SELECT  * FROM students.employee;
