import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())

instrument = rm.open_resource('GPIB0::28::INSTR')  # instrument address attenuator
idn = instrument.query('*IND?')
print(f'Device ID:{idn}')

instrument = rm.open_resource('GPIB0::6::INSTR')  # instrument address lightwave multimeter
# Querying Instrument Identification
idn = instrument.query('*IND?')
print(f'Device ID:{idn}')

# Self-Test Query
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.query('*TST?')

# Clear Status Command
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.write('*CLS')

# Standard Event Status Enable Command
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.write('*ESE')

# Standard Event Status Enable query
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.query('*ESE?')

# Standard Event Status Register query
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.query('*ESR?')

# Options query
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.query('*OPT?')
print(f'Device ID:{idn}')
# Device ID:High Performance,0,0

instrument = rm.open_resource('GPIB0::6::INSTR') # instrument address change
idn = instrument.query('*OPT?')
print(f'Device ID:{idn}')
# Device ID: , 81635A

# Wait command
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.write('*WAI')

# Read status byte query
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.query('*STB?')

# Operation complete command
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.write('*OPC')

# Operation complete query
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.query('*OPC?')

## To read attenuator value
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.query('INPUT:ATT?')
print(f'Device ID:{idn}')
# Device ID:+2.50000000E+000

## To read the wavelength value
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.query('INPUT:WAV?')
print(f'Device ID:{idn}')
# Device ID:+1.31000000E-006

# Returns a list of all GPIB commands
instrument = rm.open_resource('GPIB0::6::INSTR')
idn = instrument.query(':SYST:HELP:HEAD')
print(f'Device ID:{idn}')

# Display Brightness 0/1
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.write('DISP:BRIG 0')

# Display Enable 0/1
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.write('DISP:ENAB 0')

# set the Attenuator value
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.query(':INPUT:ATT 1.200 DB')

# It Display the "LAMBDCAL"
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.write('INP:LCM ON')

# Turning the Output On/Off of the power supply or signal generator.
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.query('OUTP ON')  # OUTP ON/ OUTP OFF
print(f'Device ID:{idn}')

# Set the Lambda Value
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.write('INPUT:WAV 1550 NM')

# Resetting an instrument
instrument = rm.open_resource('GPIB0::28::INSTR')
idn = instrument.query('*RST')

# It Display the "LAMBDCAL"
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.write('INP:LCM ON')

# It Display the Calibrate Values
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.write(':IND:OFFS:DISP')

# Turning the Calibrate On/Off
instrument = rm.open_resource('GPIB0::28::INSTR')
instrument.write(':IND:APM OFF')
