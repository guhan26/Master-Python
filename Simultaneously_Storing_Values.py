import time
import pyvisa
from datetime import datetime
import os
import csv
rm = pyvisa.ResourceManager()
voa = rm.open_resource('GPIB0::24::INSTR')
voa_2 = rm.open_resource('GPIB0::23::INSTR')
power_meter = rm.open_resource('GPIB0::20::INSTR')
Lightwave_switch = rm.open_resource('GPIB0::2::INSTR')


def set_switch():
    Lightwave_switch.write(":ROUTE:LAYER:CHANNEL A1,B2")

def set_switch_monitor():
    Lightwave_switch.write(":ROUTE:LAYER:CHANNEL A1,B4")

def read_power_chan_one():
    set_switch()

    power = power_meter.query(":FETCH2:CHAN1:SCAL:POW?")
    return float(power.strip())

read_power_chan_one()

def read_power_chan_two():
    set_switch_monitor()

    power = power_meter.query(":FETCH2:CHAN2:SCAL:POW?")
    return float(power.strip())

read_power_chan_two()
#def in_out():
 #   return

def att_one():
    data = []

    #time.sleep(3)
    Attenuation = 0.0
    while Attenuation < 5:
        Attenuation += 0.5  # Increases the attenuation by 0.5 dB in each iteration
        voa.write(f':INPUT:ATT {Attenuation}DB')
        # voa_2.write(f':INPUT:ATT {Attenuation_one} DB')
        time.sleep(1)
        # i += 0.5
        power = read_power_chan_one()
        time.sleep(1)
        values = f"Attenuation {Attenuation:.3f} dB Measured power: {power} dBm "
        data.append([Attenuation, power])
    return data

def att_two():
    data_two = []
    #time.sleep(3)
    Attenuation_two = 0.0
    while Attenuation_two < 5:
        Attenuation_two += 0.5  # Increases the attenuation by 0.5 dB in each iteration

        voa_2.write(f':INPUT:ATT {Attenuation_two}DB')
        # voa_2.write(f':INPUT:ATT {Attenuation_one} DB')
        time.sleep(1)
        # i += 0.5
        power = read_power_chan_two()
        time.sleep(1)
        values = f"Attenuation {Attenuation_two:.3f} dB Measured power: {power} dBm "
        data_two.append([Attenuation_two, power])
    return data_two

def csv_file():
    directory = "Measurement_optical"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create a CSV file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(directory, f"Measurement_{timestamp}.csv")
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Attenuator (DB)","Power (DBM)","Attenuator_two (DB)","Monitor_Power (DBM)"])

        first_att = att_one()
        second_att = att_two()

        writer.writerows(first_att)
        writer.writerows(second_att)
    print(f"Data successfully written to {filename}")

def main():

    csv_file()

if __name__ == "__main__":
    main()
