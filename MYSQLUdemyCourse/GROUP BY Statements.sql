
-- Aggregate function is used tocalculation on a set of values, and returns a single value
SELECT avg(EmpAge) FROM students.employee;

-- GROUP BY allows us to aggregate columns per some category
SELECT EmpID,EmpName,SUM(EmpAge) FROM students.employee
GROUP BY EmpID,EmpName ORDER BY SUM(EmpAge) ASC;

-- HAVING clause is used if we need to filter the result set based on aggregate functions
SELECT EmpID,SUM(EmpAge) FROM students.employee
GROUP BY EmpID
HAVING SUM(EmpAge) >23 
