import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())

# SCPI Commands for 8163A lightwave multimeter

# Sets the power measurement unit to dBm
power_channel1 = instrument_multimeter.query('SENS2:CHAN1:POW:UNIT DBM')
print(f'Device :{power_channel1}')

# Measure power on Channel 1 (Input 1)
power_channel1 = instrument_multimeter.query('READ2:CHAN1:POW?')
print(f'Device :{power_channel1}')

# To read the wavelength value in the lightwave multimeter
power_channel1 = instrument_multimeter.query(':SENS2:CHAN1:POW:WAV?')
print(f'Device :{power_channel1}')

# Returns whether the module slot is empty
power_channel1 = instrument_multimeter.query('SLOT2:EMPT?')
print(f'Device :{power_channel1}')

# Returns information about the module
power_channel1 = instrument_multimeter.query('SLOT2:IDN?')
print(f'Device :{power_channel1}')

# Returns whether an optical head is connected
power_channel1 = instrument_multimeter.query('slot2:head:empt?')
print(f'Device :{power_channel1}')

# Returns the latest selftest results for a module
power_channel1 = instrument_multimeter.query('slot2:tst?')
print(f'Device :{power_channel1}')

# Returns information about the optical head
power_channel1 = instrument_multimeter.query('slot2:head:idn?')
print(f'Device :{power_channel1}')

# 86060C Lightwave switch SCPI Commands

# Test sending a route command if this is the correct instrument
# Ensure that this command is applicable to the connected device
instrument_multimeter = rm.open_resource('GPIB0::2::INSTR')
multimeter_idn = instrument_multimeter.write(':ROUTE:LAYER:CHANNEL A1,B7')
print(f"Multimeter ID: {multimeter_idn}")

# Check for Errors: To query the error status
power_channel2 = instrument_multimeter.query('SYST:ERR?')
print(f"Measured power on Input 2 (Channel 2): {power_channel2.strip()}")

# SCPI Commands for 8156A optical attenuator

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
instrument = rm.open_resource('GPIB0::28::INSTR')
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
