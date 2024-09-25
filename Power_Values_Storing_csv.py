import time
import pyvisa
from datetime import datetime
import os
import csv

# Initialize VISA resource manager
rm = pyvisa.ResourceManager()
voa = rm.open_resource('GPIB0::24::INSTR') # VOA instrument GPIB address
#voa_2 = rm.open_resource('GPIB0::23::INSTR') # Power Meter GPIB address
power_meter = rm.open_resource('GPIB0::20::INSTR')

def read_power():

    power = power_meter.query(":FETCH2:CHAN1:SCAL:POW?")
    return float(power.strip())

read_power()

# Create directory for storing data if it doesn't exist
directory = "Measurement_file"
if not os.path.exists(directory):
    os.makedirs(directory)

# Create a CSV file with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = os.path.join(directory, f"Measurement_{timestamp}.csv")

# Open the CSV file for writing
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Attenuation (dB)", "Power (dBm)"])

    # The attenuation starts at 0 dB
    Attenuation = 0.0
    while Attenuation <= 5:
        Attenuation += 0.5 # Increases the attenuation by 0.5 dB in each iteration
        # Set attenuation on VOA
        voa.write(f':INPUT:ATT {Attenuation}DB')
        time.sleep(3)
        # i += 0.5
        # Read corresponding power value from Power Meter
        power = read_power()
        time.sleep(3)
        print(f"Attenuation {Attenuation:.3f} dB Measured power: {power} dBm")     
        # Record attenuation, power
        writer.writerow([Attenuation, power])

print(f"Data saved to {filename}")


