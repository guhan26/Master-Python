-- CASE

SELECT EmpName,
CASE 
    WHEN(EmpID <= 5) THEN 'premium'
    WHEN(EmpID BETWEEN 2 AND 6) THEN 'PLUS'
    ELSE 'Normal'    
END
FROM students.employee;

-- import and Export

CREATE TABLE simple(
a INTEGER,
b INTEGER,
c INTEGER
);

SELECT * FROM students.simple;
