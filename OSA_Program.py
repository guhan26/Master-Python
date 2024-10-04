import pyvisa
import csv
import time
from datetime import datetime
import os

# Connect to the OSA
rm = pyvisa.ResourceManager()
osa = rm.open_resource('GPIB0::8::INSTR')  # Replace with actual GPIB address


def reset_osa():
    osa.write('*RST')
    time.sleep(3)


def check_response():
    response = osa.query('*IDN?')
    print(f'OSA Response: {response}')
    time.sleep(0.1)


def configure_osa():
    osa.write('STA 1305')  # Start Wavelength
    time.sleep(0.1)
    osa.write('CNT 1310')  # Center Wavelength
    time.sleep(0.1)
    osa.write('STO 1315')  # Stop Wavelength
    time.sleep(0.1)
    osa.write('RLV 0')  # Set reference level
    time.sleep(0.1)
    osa.write('LOG 10')  # Set scale, say log(/div)
    time.sleep(0.1)
    osa.write('ATT OFF')  # Set optical attenuation
    time.sleep(0.1)
    osa.write('RES 0.1')  # Set resolution
    time.sleep(0.1)
    osa.write('VBW 1KHz')  # Set videoBandwidth
    time.sleep(0.1)
    osa.write('AVT 10')  # Set Point Average
    time.sleep(0.1)
    osa.write('AVS 5')  # Set Sweep Average
    time.sleep(0.1)
    osa.write('SMT OFF')  # Set Smoothing Point
    time.sleep(0.1)
    osa.write('MPT 501')  # Set Sampling Points
    time.sleep(0.1)
    osa.write('ARES OFF')  # Set Actual-Resolution
    time.sleep(0.1)


def perform_single_sweep():
    osa.write('SSI')  # Perform single sweep
    time.sleep(15)  # Wait for sweep to complete and include delay (Sweep time + additional delay)


def peak_search():
    osa.write('PKS PEAK')  # Peak Search
    time.sleep(1)
    central_peak_wavelength = osa.query('CNT?')
    time.sleep(1)
    # Strip any unwanted characters like '\r\n'
    central_wavelength = central_peak_wavelength.strip().split(',')
    return float(central_wavelength[0])


def spectral_width_measurement_20dB():
    osa.write('ANA THR, 20')  # Spectral Width Measurement at 20 dB
    time.sleep(1)
    spectral_width_20dB = osa.query('ANAR?')
    time.sleep(1)

    # Split the response by comma
    wavelength_values = spectral_width_20dB.strip().split(',')

    # Convert both values to float and return them
    return float(wavelength_values[0]), float(wavelength_values[1])


def measure_smsr():
    osa.write('ANA SMSR, LEFT')  # Measure Side Mode Suppression Ratio (SMSR)
    time.sleep(1)
    second_peak_wavelength = osa.query('ANAR?')
    time.sleep(1)

    # Split the response by comma
    smsr_values = second_peak_wavelength.strip().split(',')

    # Return both values as floats if needed (or adjust based on your requirements)
    # In this case, the first value might be the SMSR ratio and the second the wavelength
    return float(smsr_values[0]), float(smsr_values[1])


def save_results(folder_path='osa_measurements'):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate filename with timestamp
    filename = os.path.join(folder_path, f'osa_measurements_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')

    # Write results to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Central Peak Wavelength (nm)', '20 dB Wavelength (nm)', 'SMSR Wavelength (nm)'])

        # Collect the measurements
        central_peak = peak_search()
        loss_20dB = spectral_width_measurement_20dB()
        smsr_wavelength = measure_smsr()

        # Save the results to a CSV file
        results = [central_peak, loss_20dB, smsr_wavelength]
        writer.writerow(results)

    print(f'Results saved to {filename}')


def main():
    check_response()
    configure_osa()
    perform_single_sweep()
    save_results()


if __name__ == '__main__':
    main()
