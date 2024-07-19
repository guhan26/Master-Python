/* This is the simple basic sql query, How to create, insert, select, alter, update, delete and all join */

-- creating table and assigning attribute
create table mydatabase.students ( student_id int, student_firstname varchar(255) , student_lastname varchar(255)  ,PRIMARY KEY (student_id));

-- commit is save all the changes made
commit;

-- Drop is used to delete a whole database or a table
drop table mydatabase.students;

-- insert statement writes new rows of data into a table
insert into mydatabase.students values ( 01 ,'Guhan','v');
insert into mydatabase.students values ( 02 ,'Arun','a');
insert into mydatabase.students values ( 03 ,'Kavin','r');
insert into mydatabase.students values ( 04 ,'Ram','t');

-- select command is used to view database or a table
SELECT * FROM mydatabase.students;

-- Alter is used to update the structure of the table in the database
-- ADD is command used to add a new column to the existing database table  
ALTER TABLE mydatabase.students
ADD PRIMARY KEY (student_id);

-- Update statement changes the data of one or more records in a table
-- set is command is used with UPDATE to specify which columns and values that should be updated in a table
-- WHERE is used to filter records 
update mydatabase.students
set student_firstname =Arun
where student_id=02;

-- Delete is command that is used to remove the records present in a table
delete from mydatabase.students 
where student_id=02;

-- create table mydatabase.students_add ( student_roll int, student_Dob varchar(255) , student_city varchar(255)  ,PRIMARY KEY (student_roll));
-- commit;
-- drop table mydatabase.students_add;
insert into mydatabase.students_add values ( 01 ,'2/01/2032','AAA');
insert into mydatabase.students_add values ( 02 ,'4/04/2045','BBB');
insert into mydatabase.students_add values ( 03 ,'9/01/2029','CCC');
insert into mydatabase.students_add values ( 04 ,'7/03/2043','DDD');
SELECT * FROM mydatabase.students_add;*/

-- SELECT is Defines the columns to be retrieved from the joined tables
-- FROM is Specifies the first table from which you want to retrieve data
-- ON is Specifies the condition for matching rows between tables
--  INNER JOIN, LEFT JOIN, RIGHT JOIN, and SELF JOIN
-- Join is a command used to combines records from two or more tables in a database
SELECT mydatabase.students.student_id,mydatabase.students_add.student_roll 
FROM mydatabase.students
right JOIN mydatabase.students_add ON mydatabase.students.student_firstname = mydatabase.students_add.student_Dob;
