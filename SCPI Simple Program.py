# simple program to measure power

import mysql.connector
import pyvisa
import time

# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GuhanV@1234",
    database="optiqual"
)
mycursor = mydb.cursor()

# SQL query for inserting data
sqlFormula = "INSERT INTO students (ATT_Values, POWER_Values) VALUES (%s, %s)"

# PyVISA connection to the HP8163A (for power measurement)
rm = pyvisa.ResourceManager()

# Connect to the HP8163A (Power meter)
power_meter = rm.open_resource('GPIB0::20::INSTR')

# Connect to the HP8156A (Attenuator)
attenuator = rm.open_resource('GPIB0::24::INSTR')

# Loop to set attenuation and measure power
i = 1
while i <= 5:
    time.sleep(3)

    # Set attenuation on the attenuator
    attenuator.write(f':INPUT:ATT {i}DB')

    # Measure power on the power meter
    time.sleep(3)
    power_str = power_meter.query("READ2:POW?")  # Get the power measurement in dBm
    power = float(power_str.strip())  # Convert the string to a float


    # Insert the attenuation and power values into the database
    students = [(i, power)]  # Prepare the values to insert
    mycursor.executemany(sqlFormula, students)  # Execute the insertion
    mydb.commit()  # Commit the transaction

    print(f"Attenuation: {i} dB, Power: {power} dBm")

    i += 1  # Increment the attenuation value

# Close database and instrument connections
mydb.close()
attenuator.close()
power_meter.close()


OUTPUT:
Attenuation: 1 dB, Power: -6.226089 dBm
Attenuation: 2 dB, Power: -7.190531 dBm
Attenuation: 3 dB, Power: -8.171294 dBm
Attenuation: 4 dB, Power: -9.166146 dBm
Attenuation: 5 dB, Power: -10.15291 dBm
