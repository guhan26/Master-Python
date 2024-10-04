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


def read_power_chan_two():
    set_switch_monitor()
    power = power_meter.query(":FETCH2:CHAN2:SCAL:POW?")
    return float(power.strip())


def att_one():
    data = []
    Attenuation = 0.0
    while Attenuation < 5:
        Attenuation += 0.5
        voa.write(f':INPUT:ATT {Attenuation}DB')
        time.sleep(1)
        power = read_power_chan_one()
        time.sleep(1)
        data.append([Attenuation, power])
    return data


def att_two():
    data_two = []
    Attenuation_two = 0.0
    while Attenuation_two < 5:
        Attenuation_two += 0.5
        voa_2.write(f':INPUT:ATT {Attenuation_two}DB')
        time.sleep(1)
        power = read_power_chan_two()
        time.sleep(1)
        data_two.append([Attenuation_two, power])
    return data_two


def csv_file():
    directory = "Measurement_optical_AM"
    if not os.path.exists(directory):
        os.makedirs(directory)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(directory, f"Measurement_{timestamp}.csv")

    # Get data from both attenuation functions
    first_att = att_one()
    second_att = att_two()

    # Ensure both lists have the same length
    min_length = min(len(first_att), len(second_att))
    combined_data = []

    for i in range(min_length):
        combined_row = first_att[i] + second_att[i]  # Combine results row by row
        combined_data.append(combined_row)

    # Write the data to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Attenuator (DB)", "Power (DBM)", "Attenuator_two (DB)", "Monitor_Power (DBM)"])
        writer.writerows(combined_data)

    print(f"Data successfully written to {filename}")


def main():
    csv_file()


if __name__ == "__main__":
    main()
