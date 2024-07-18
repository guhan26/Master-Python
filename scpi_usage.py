import pyvisa

# Connect to instrument
# Initialize PyVISA resource manager

rm = pyvisa.ResourceManager()

# Open a connection to the instrument

instrument = rm.open_resource('TCPIP0::192.168.1.100::inst0::INSTR')  # Replace with your instrument's address

# Check if instrument is connected
print(instrument.query('*IDN?'))

# reset the device
reset_inst = instrument.query('*RST?')
print(reset_inst)

# Clear register
reset_inst=instrument.query('*CLS')
print(reset_inst)

# test result
reset_inst=instrument.query('*TST?')
print(reset_inst)
# Set frequency
instrument.write('SOURce1:FREQuency 1000 MHz')

# Query output power
response = instrument.query('MEASure1:POWer?')
print('Output Power: ', response)

# Measurement Commands

# measurement operation
reset_inst=instrument.query('MEASure')
print(reset_inst)

# measurement results
reset_inst=instrument.query('FETCh?')
print(reset_inst)

# Read data
reset_inst=instrument.query('READ?')
print(reset_inst)

# Configuration Commands

# Configure measurement
reset_inst=instrument.query('CONF')
print(reset_inst)

# configuring specific instrument functionalities

reset_inst=instrument.query('CONFigure')
print(reset_inst)

# Query Commands
reset_inst=instrument.query('*OPC?')
print(reset_inst)

# Data Transfer Commands
reset_inst=instrument.query('DATA')
print(reset_inst)

#  Output data
reset_inst=instrument.query('OUTPUT')
print(reset_inst)

# Control Commands

# measurement
reset_inst=instrument.query('INITiate')
print(reset_inst)

# action in progress
reset_inst=instrument.query('ABORt')
print(reset_inst)

# control triggering
reset_inst=instrument.query('TRIGger')
print(reset_inst)

# Error and Event Handling Commands
# disable service request (SRQ) events
reset_inst=instrument.query('*SRE')
print(reset_inst)

#
reset_inst=instrument.query('*ESE')
print(reset_inst)

# error handling Exceptions try
try:

    # Attempt to communicate with the instrument
    # Query the instrument identification

    response = instrument.query('*IDN?')

    # Print the response error handling Exceptions except
    print('Instrument Identification:', response.strip())
except pyvisa.VisaIOError as e:
    print(f'Error communicating with the instrument: {e}')

# Close the connection
instrument.close()
