
-- Create Table
CREATE TABLE accounts(user_id int primary key, username varchar(255),email varchar(255));

-- Insert
INSERT INTO accounts VALUES(01 , 'Guhan','guhan12@gmail.com');
INSERT INTO accounts VALUES(02 , 'Arun','arun34@gmail.com');
INSERT INTO accounts VALUES(03 , 'Kavin','kavin81@gmail.com');
INSERT INTO accounts VALUES(04 , 'Ram','ram21@gmail.com');

-- UPDATE
UPDATE accounts
SET username = 'varun'
WHERE user_id = 3;

-- DELETE
DELETE FROM accounts
WHERE user_id = 2;

-- ALTER TABLE
ALTER TABLE accounts
ADD userphonenumber int;

-- DROP TABLE
DROP TABLE accounts;

-- SELECT
SELECT * FROM accounts

