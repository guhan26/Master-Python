# Importing tabulate Modules
from tabulate import tabulate
# Import MySQL Connector Python module
import mysql.connector

# connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    database="mydatabase",
    user="root",
    password="guhan"
)


# Function to insert a new student record
def insert(student_id, student_firstname, student_lastname):

    res = connection.cursor()
    sql = "insert into mydatabase.students (student_id, student_firstname, student_lastname) values (%s,%s,%s)"
    students = (student_id, student_firstname, student_lastname)
    res.execute(sql, students)
    # commit is save all the changes made in the database
    connection.commit()
    print("Data is Insert")


# Function to update an existing student record
def update(student_id, student_firstname, student_lastname):
    res = connection.cursor()
    sql = "update mydatabase.students set student_id=%s, student_firstname=%s, student_lastname=%s"
    students = (student_id, student_firstname, student_lastname)
    res.execute(sql, students)
    # commit is save all the changes made in the database
    connection.commit()
    print("Data is Update")


# Function to select and display all student records
def select(student_id, student_firstname, student_lastname):
    res = connection.cursor()
    sql = "SELECT student_id, student_firstname, student_lastname from students"
    res.execute(sql)
    # Fetch all rows from the result set
    result = res.fetchall()
    # headers is table to be clear format
    print(tabulate(result, headers=["student_id", "student_firstname", "student_lastname"]))


# Function to delete a student record
def delete(id):
    res = connection.cursor()
    sql = "delete from students where idd=%s"
    students = (id,)
    res.execute(sql, students)
    # commit is save all the changes made in the database
    connection.commit()
    print("Data Delete")


# Main program loop
while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    # Prompt user for choice
    choice = int(input("Enter your Choice : "))
    if choice == 1:
        student_id = input("Enter the Student_id : ")
        student_firstname = input("Enter the Student_firstname : ")
        student_lastname = input("Enter the Student_lastname : ")
        # Calling insert function
        insert(student_id, student_firstname, student_lastname)
    elif choice == 2:
        student_id = input("Enter the Student_id : ")
        student_firstname = input("Enter the Student_firstname : ")
        student_lastname = input("Enter the Student_lastname : ")
        # Calling update function
        update(student_id, student_firstname, student_lastname)
    # Example arguments for select function
    elif choice == 3:
        select(1, 'Guhan', 'v')
    # Calling delete function
    elif choice == 4:
        id = input("Enter the student_id to Delete : ")
        delete(id)
    # Exit the program
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection")
