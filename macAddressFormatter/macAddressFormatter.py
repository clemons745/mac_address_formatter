#! /usr/bin/python3

#####
#
# Name: macAddressFormatter.py
#
# Description: Changes the format of a given list of mac addresses
#
# Version: 1.3
#
# Date of last update: 4/16/2018
#
# Expected Input: List of mac address (1 per line)
#
# Expected Output: List of formatted mac addresses
#
# Author: Tony Clemons (clemons745@gmail.com)
#
#####

# Import the needed Modules
from mac_format_module import change_mac_address_format, isValidMacAddress
import sys
import logging
import os

# Setup Logging
logging.basicConfig(filename='logfile.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of Program')
# Uncomment the line below to disable logging
# logging.disable(logging.CRITICAL)

# Collect the list of mac addresses from the user
# Also make sure the user actually specifies a file
try:
    unformattedFilename = sys.argv[1]
    logging.info('''unformattedFile collected \
successfully as filename %s''' % unformattedFilename)

except IndexError:
    logging.critical('''User did not specify file of \
mac address to be converted.''')
    raise Exception('No file specified')

# Make sure the file exists
if not os.path.exists(unformattedFilename):
    logging.critical('The file the user specified does not exist.')
    raise Exception('Specified file does not exist')

# Find out what format the user wants the mac addresses in
# Possible Options
#
# 000000000000
# 00.00.00.00.00.00
# 0000.0000.0000
# 000.000.000.000
# 00:00:00:00:00:00
# 0000:0000:0000
# 00-00-00-00-00-00

print('''This program will take the list of mac addresses storged in %s \
 and convert them to a desired format and store the new list in a text \
 file called "Formatted_Mac_Addresses.txt" \
 in this directory.\n''' % unformattedFilename)

while True:
    print('''What format do you want your mac addresses in?
1 000000000000
2 00:00:00:00:00:00
3 0000.0000.0000
4 00-00-00-00-00-00
5 00.00.00.00.00.00
6 0000:0000:0000
7 000.000.000.000

Selection Number: ''', end='')

    desiredFormatSelection = input()

    # Check to ensure the users selection is a valid selection
    if not desiredFormatSelection.isdecimal():  # ensure they entered a number
        print('\nSelection not valid.\n')
        logging.error('''User entered "%s" which is not a \
number.''' % desiredFormatSelection)
        continue

    # Ensure the selection is a valid option
    elif int(desiredFormatSelection) < 1 or int(desiredFormatSelection) > 7:
        print('\nSelection not valid.\n')
        logging.error('''User entered "%s" which is not a \
valid selection.''' % desiredFormatSelection)
        continue

    else:  # If this code executes, the selection was valid
        logging.info('''User selected "%s" which is a \
        valid selection.''' % desiredFormatSelection)
        break

# Check if Formatted_Mac_Addresses.txt already exists.
# If so, warn the user of this and ask if they would like to continue.
if os.path.exists('Formatted_Mac_Addresses.txt'):
    logging.warning('''"Formatted_Mac_Addresses.txt" already exists. \
Asking the user if they would like to continue.''')
    print('''WARNING: "Formatted_Mac_Addresses.txt" already exists. \
The new list of mac addresses will be appended to the end of it. \
Would you like to continue?
1 Yes
2 No

Selection Number: ''', end='')
    continueWithConversion = input()
    while True:
        if continueWithConversion == '1':
            logging.warning('''User has selected to continue with conversion \
even though "Formatted_Mac_Addresses.txt" already exists.''')
            break
        elif continueWithConversion == '2':
            logging.warning('''User has selected not to continue with \
conversion because "Formatted_Mac_Addresses.txt" already exists.''')
            sys.exit()
        else:
            logging.error('''User input %s, which is not a valid selection \
when asked if they would like to continue.''' % continueWithConversion)
            print('''Invalid Selection.  Please enter "1" or "2".

Selection Number: ''', end='')
            continueWithConversion = input()

# Get mac addresses from the file into a list
# Then close the file as it is not needed anymore
unformattedFile = open(unformattedFilename, 'r')  # Open the file
unformattedFile.seek(0)  # Ensure we start at the top of the list
unformattedMacList = unformattedFile.readlines()  # Read Unformatted MACs
macList = []
unformattedFile.close()  # close the file, it is no longer needed

for i in range(len(unformattedMacList)):
    macList.append(unformattedMacList[i].strip())
logging.info('MAC Addresses parsed from file, now formatting.')

# Convert the mac addresses and save them to a new list
formattedMacAddresses = []
isErrorFound = False

for mac in macList:

    # Ensure mac is valid and in a supportted format
    if not isValidMacAddress(mac):
        formattedMacAddresses.append('''%s is either not a mac address, \
or the format is not supported.''' % mac)
        logging.error('''"%s" is either not a MAC Address, \
or the format is not supported.''' % mac)
        isErrorFound = True
        continue

    if desiredFormatSelection == '1':
        formattedMacAddresses.append(
            change_mac_address_format(mac, '000000000000'))
        logging.info(
            'Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')

    elif desiredFormatSelection == '2':
        formattedMacAddresses.append(
            change_mac_address_format(mac, '00:00:00:00:00:00'))
        logging.info(
            'Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')

    elif desiredFormatSelection == '3':
        formattedMacAddresses.append(
            change_mac_address_format(mac, '0000.0000.0000'))
        logging.info(
            'Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')

    elif desiredFormatSelection == '4':
        formattedMacAddresses.append(
            change_mac_address_format(mac, '00-00-00-00-00-00'))
        logging.info(
            'Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')

    elif desiredFormatSelection == '5':
        formattedMacAddresses.append(
            change_mac_address_format(mac, '00.00.00.00.00.00'))
        logging.info(
            'Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')

    elif desiredFormatSelection == '6':
        formattedMacAddresses.append(
            change_mac_address_format(mac, '0000:0000:0000'))
        logging.info(
            'Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')

    elif desiredFormatSelection == '7':
        formattedMacAddresses.append(
            change_mac_address_format(mac, '000.000.000.000'))
        logging.info(
            'Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')

    else:
        logging.critical('''Invalid Selection detected at formatting stage, selection was "%s". \
This exception should never trigger \
unless there is a bug in the code.''' % desiredFormatSelection)
        assert desiredFormatSelection >= 1 and desiredFormatSelection <= 7

# Save list of new format to a file
newMacAddressFile = open('Formatted_Mac_Addresses.txt', 'a')
logging.info('Created file named "Formatted_Mac_Addresses.txt"')

for mac in formattedMacAddresses:
    newMacAddressFile.write(mac + '\n')
    logging.info('Wrote "' + mac + '" to file')

# Close the file as it is no longer needed
newMacAddressFile.close()
logging.info('Closed file named "Formatted_Mac_Addresses.txt"')

# Let the user know that the process is complete.
print('''\n\nMac Address have been formatted and saved in a file \
called "Formatted_Mac_Addresses.txt" and saved in this directory.''')

# If any errors were found, notify the user
if isErrorFound:
    print('''There were problems converting the format of some of the \
MAC Addresses.  These were still saved to the new file with a message. \
See logfile.txt for more information.''')
logging.debug('End of Progam')
