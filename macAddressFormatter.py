#! /usr/bin/python3

#####
#
# Name: macAddressFormatter.py
#
# Description: Changes the format of a given list of mac addresses
#
# Version: 1.2
#
# Date: 4/9/2018
#
# Expected Input: List of mac address (1 per line)
#
# Expected Output: List of formatted mac addresses
#
# Author: Tony Clemons (clemons745@gmail.com)
#
#####

from mac_format_module import *
import sys, logging, os

logging.basicConfig(filename='logfile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Uncomment the line below to disable logging
#logging.disable(logging.CRITICAL)

logging.debug('Start of Program')

# Collect the list of mac addresses from the user
# Also make sure the user actually specifies a file

try:
	unformattedFilename = sys.argv[1]
	logging.info('unformattedFile collected successfully as filename ' + unformattedFilename)
except:
	logging.critical('User did not specify file of mac address to be converted.')
	raise Exception('No file specified')

#Make sure the file exists

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
	
	if not desiredFormatSelection.isdecimal():  #ensure they entered a number
		print('\nSelection not valid.\n')
		logging.error('User entered "' + desiredFormatSelection + '" which is not a number.')
		continue
	elif int(desiredFormatSelection) < 1 or int(desiredFormatSelection) > 7: #ensure the selection is a valid option
		print('\nSelection not valid.\n')
		logging.error('User entered "' + desiredFormatSelection + '" which is not a valid selection.')
		continue
	else:	#If this code executes, the selection was valid
		logging.info('User selected "' + desiredFormatSelection + '" which is a valid selection.')
		break

# Get mac addresses from the file into a list
unformattedFile = open(unformattedFilename, 'r')
unformattedMacList = unformattedFile.readlines()
macList = []

for i in range(len(unformattedMacList)):
	macList.append(unformattedMacList[i].strip())
logging.info('MAC Addresses parsed from file, now formatting.')

# Convert the mac addresses and save them to a new list

formattedMacAddresses = []
isErrorFound = False

for mac in macList:

	if isValidMacAddress(mac) == False: 			#check to see if the item really is a mac address, and if it is a supported format
		formattedMacAddresses.append(mac + ' is either not a mac address, or the format is not supported.')
		logging.error('"' + mac + '" is either not a MAC Address, or the format is not supported.')
		isErrorFound = True
		continue

	if desiredFormatSelection == '1':
		formattedMacAddresses.append(change_mac_address_format(mac, '000000000000'))
		logging.info('Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')
	
	elif desiredFormatSelection == '2':
		formattedMacAddresses.append(change_mac_address_format(mac, '00:00:00:00:00:00'))
		logging.info('Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')
	
	elif desiredFormatSelection == '3':
		formattedMacAddresses.append(change_mac_address_format(mac, '0000.0000.0000'))
		logging.info('Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')
	
	elif desiredFormatSelection == '4':
		formattedMacAddresses.append(change_mac_address_format(mac, '00-00-00-00-00-00'))
		logging.info('Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')
	
	elif desiredFormatSelection == '5':
		formattedMacAddresses.append(change_mac_address_format(mac, '00.00.00.00.00.00'))
		logging.info('Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')		
	
	elif desiredFormatSelection == '6':
		formattedMacAddresses.append(change_mac_address_format(mac, '0000:0000:0000'))
		logging.info('Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')
	
	elif desiredFormatSelection == '7':
		formattedMacAddresses.append(change_mac_address_format(mac, '000.000.000.000'))
		logging.info('Converted "' + mac + '" to "' + formattedMacAddresses[-1] + '"')
	
	else:
		logging.critical('Invalid Selection detected at formatting stage, selection was "' + desiredFormatSelection + '".  This exception should never trigger unless there is a bug in the code.')
		raise Exception('Invalid Selection while formatting MAC address.  This exception should never trigger unless there is a bug in the code.')

# Save list of new format to a file

newMacAddressFile = open('Formatted_Mac_Addresses.txt', 'a')
logging.info('Created file named "Formatted_Mac_Addresses.txt"')

for mac in formattedMacAddresses:
	newMacAddressFile.write(mac + '\n')
	logging.info('Wrote "' + mac + '" to file')

newMacAddressFile.close()
logging.info('Closed file named "Formatted_Mac_Addresses.txt"')

# Let the user know that the process is complete.

print('\n\nMac Address have been formatted and saved in a file called "Formatted_Mac_Addresses.txt" and saved in this directory.')

if isErrorFound:
	print('There were problems converting the format of some of the MAC Addresses.  These were still saved to the new file with a message.  See logfile.txt for more information.')

logging.debug('End of Progam')
