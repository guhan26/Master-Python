import pyvisa
import time
import csv
from datetime import datetime
import os

# Initialize GPIB interface and connect to DCA mainframe
rm = pyvisa.ResourceManager()
dca = rm.open_resource('GPIB0::7::INSTR')  # Replace '7' with the actual GPIB address of the DCA

def Mode_Configuration():

    dca.write('CHAN1:DISP ON')
    dca.write('SYST:MODE OSC')
    dca.write('AUT')
    dca.write('*WAI')
    print("Mode configuration complete.")


def set_wavelength():

    # Set Wavelength on Channel 1
    dca.write('CHAN1:WAV 1310')
    wavelength = dca.query('CHAN1:WAV?')  # Remove any whitespace/newline
    numeric_value = wavelength.split(',')[1]
    return float(numeric_value)



def other_configurations():

    # Set Filter and other configurations
    dca.write('CHAN1:FSEL FILTER2')
    dca.write('CHAN1:FILT ON')
    dca.write('TRIG:SOUR FPAN')
    dca.write('TRIG:BWL HIGH')
    dca.write('DISP:PERS CGR')
    dca.write('MEAS:DEF THR, STAN')
    dca.write('MEAS:DEF EWIN, 40, 60')
    dca.write('MEAS:ANN ON')
    dca.write('*WAI')
    print("Other configurations applied.")

def amplitude():

    vamp = dca.query('MEAS:VAMP? CHAN1').strip()
    return float(vamp)

def eye_mask_mode():

    dca.write('SYST:MODE EYE')
    dca.write('DISP:PERS CGR')
    dca.write('MEAS:ANN ON')
    dca.write('*WAI')
    print("Switched to Eye Mask Mode.")

def extinction_ratio():

    extinction_ratio = dca.query('MEAS:CGR:ERAT? DEC').strip()
    return float(extinction_ratio)


def load_eye_mask():
    # Load eye mask and perform alignment
    dca.write('MTES:LOAD "10GbE_10_3125_May02.msk"')
    dca.write('MTES:ALIG')
    dca.write('MTES:AOPT ON')
    dca.write('MTES:TEST ON')
    dca.write('*WAI')
    print("Eye mask loaded.")

def _waveforms():

    while True:
        waveform_count = int(float(dca.query('MTES:COUN:WAV?').strip()))  # Handle scientific notation
        time.sleep(1)
        if waveform_count >= 1000:
            return float(1000)
            break

def Failed_samples():

    failed_samples = dca.query('MTES:COUN:FSAM?').strip()
    return float(failed_samples)

def Failed_Samples_Regions():

    region_1 = dca.query('MTES:COUN:FAIL? REG1').strip()
    print(f"failed_samples_region_1: {region_1}")

    region_2 = dca.query('MTES:COUN:FAIL? REG2').strip()
    print(f"failed_samples_region_2: {region_2}")

    region_3 = dca.query('MTES:COUN:FAIL? REG3').strip()
    print(f"failed_samples_region_3: {region_3}")

def mask_margin_test():

    dca.write('MTES:MMAR:PERC 5')
    dca.write('*WAI')
    margin_test = dca.query('MTES:MMAR:PERC?').strip()
    return float(margin_test)
    dca.write('MTES:MMAR:STATE ON')
    dca.write('*WAI')

def total():

    total_hits = dca.query('MTES:COUN:HITS? TOT').strip()
    return float(total_hits)


def margin():

    margin_hits = dca.query('MTES:COUN:HITS? MARG').strip()
    return float(margin_hits)

def mask():

    mask_hits = dca.query('MTES:COUN:HITS? MASK').strip()
    return float(mask_hits)

def Stop_Mask_Test():

    dca.write('MTES:TEST OFF')
    print("Mask test stopped.")

def save_results(folder_path='dca_measurements'):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = os.path.join(folder_path, f'dca_measurements_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Wavelength', 'Vamp', 'Extinction Ratio', 'Waveforms', 'Failed samples', 'Mask Margin', 'Total_Hits',
                         'Margin_Hits', 'Mask_Hits'])


        wavelength = set_wavelength()
        other_configurations()
        Vamp = amplitude()
        eye_mask_mode()
        extinction = extinction_ratio()
        load_eye_mask()
        waveforms = _waveforms()
        Failed = Failed_samples()
        Failed_Samples_Regions()
        mask_margin_test()
        test1 = mask_margin_test()
        hits_total = total()
        hits_margin = margin()
        hits_mask = mask()
        Stop_Mask_Test()

        results = [wavelength, Vamp, extinction, waveforms, Failed, test1, hits_total, hits_margin, hits_mask]
        writer.writerow(results)

    print(f'Results saved to {filename}')


def main():
    Mode_Configuration()
    save_results()


if __name__ == '__main__':
    main()
