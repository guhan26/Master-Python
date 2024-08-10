
-- Aggregate function is used tocalculation on a set of values, and returns a single value
SELECT avg(EmpAge) FROM students.employee;

-- GROUP BY allows us to aggregate columns per some category
SELECT EmpID,EmpName,SUM(EmpAge) FROM students.employee
GROUP BY EmpID,EmpName ORDER BY SUM(EmpAge) ASC;

-- HAVING clause is used if we need to filter the result set based on aggregate functions
SELECT EmpID,SUM(EmpAge) FROM students.employee
GROUP BY EmpID
HAVING SUM(EmpAge) >23 

-- ASSESSMENT TEST 1

-- 1.
SELECT customer_id,SUM(amount)
FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) > 110;

-- 2.
SELECT COUNT(*) FROM film
WHERE title LIKE 'J%';

-- 3.
SELECT first_name,last_name FROM customer
WHERE first_name LIKE 'E%'
AND address_id <500
ORDER BY customer_id DESC
LIMIT 1;
