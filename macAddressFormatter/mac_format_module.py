#! /usr/bin/python3

#####
#
# Name: mac_format_module.py
#
# Description: This is a module that will format mac addresses
#
# Version: 1.3
#
# Date of last update: 4/16/2018
#
# Author: Tony Clemons (clemons745@gmail.com)
#
#####


def change_mac_address_format(oldMac, format):
    # This function changes the format of a mac address to the specified format
    oldMac = normal_mac(oldMac)  # Set the mac address to format 000000000000
    newMacList = list(oldMac)  # Break the mac address out into a list

    # The below if statement will just return oldMac as it is
    # Because it is already in 000000000000 format
    if format == '000000000000':
        return oldMac

    # the below code steps through the mac address and inserts characters as
    # needed to convert the mac address to the desired format
    elif format == '00:00:00:00:00:00':
        for i in range(2, 17, 3):
            newMacList.insert(i, ':')

    elif format == '0000.0000.0000':
        for i in range(4, 14, 5):
            newMacList.insert(i, '.')

    elif format == '00-00-00-00-00-00':
        for i in range(2, 17, 3):
            newMacList.insert(i, '-')

    elif format == '00.00.00.00.00.00':
        for i in range(2, 17, 3):
            newMacList.insert(i, '.')

    elif format == '0000:0000:0000':
        for i in range(4, 14, 5):
            newMacList.insert(i, ':')

    elif format == '000.000.000.000':
        for i in range(3, 15, 4):
            newMacList.insert(i, '.')

    elif format == '0000-0000-0000':
        for i in range(4, 14, 5):
            newMacList.insert(i, '-')

    else:
        raise Exception('Format is not supported by this module.')

    return ''.join(newMacList)  # return the newly converted mac address


def normal_mac(oldMac):
    # This function changes the format of any mac address to 0000000000000
    return oldMac.replace('-', '').replace('.', '').replace(':', '')


def isMacInCorrectFormat(mac, format):
    # This function returns True or False
    # Depending on if the file is in the format specified
    import re

    if format == '000000000000':
        macRegex = re.compile(r'^\w{12}$')
    elif format == '00:00:00:00:00:00':
        macRegex = re.compile(r'^\w{2}(:\w{2}){5}$')
    elif format == '0000.0000.0000':
        macRegex = re.compile(r'^\w{4}\.\w{4}\.\w{4}$')
    elif format == '00-00-00-00-00-00':
        macRegex = re.compile(r'^\w{2}(-\w{2}){5}$')
    elif format == '00.00.00.00.00.00':
        macRegex = re.compile(r'^\w{2}(\.\w{2}){5}$')
    elif format == '0000:0000:0000':
        macRegex = re.compile(r'^\w{4}:\w{4}:\w{4}$')
    elif format == '000.000.000.000':
        macRegex = re.compile(r'^\w{3}\.\w{3}\.\w{3}\.\w{3}$')
    elif format == '0000-0000-0000':
        macRegex = re.compile(r'^\w{4}-\w{4}-\w{4}$')
    else:
        # If we get to this else statement, the format is not supported.
        # Return False
        return False

    # check the mac address against the regex specified above,
    # Return True for False depending on result
    if macRegex.search(mac) is None:
        return False
    else:
        return True


def isValidMacAddress(mac):
    # This function returns True or False depending on if the item given
    # Is a mac address and in a supported format
    macFormatList = ["000000000000",
                     "00:00:00:00:00:00",
                     "0000.0000.0000",
                     "00-00-00-00-00-00",
                     "00.00.00.00.00.00",
                     "0000:0000:0000",
                     "000.000.000.000",
                     "0000-0000-0000"]

    for i in range(len(macFormatList)):

        if isMacInCorrectFormat(mac, macFormatList[i]):
            return True
    return False


def fetchMacVendor(mac):
    # This function looks up the vendor of a mac address.
    # Returns None if unable to find it
    try:
        from manuf import manuf
    except ImportError:
        raise Exception('''manuf dependency not installed. \
This can be installed by running "pip install manuf"''')
    import os

    if not isValidMacAddress(mac):
        return 'Not a valid mac address'

    if not isMacInCorrectFormat(mac, "00:00:00:00:00:00"):
        mac = change_mac_address_format(mac, "00:00:00:00:00:00")

    p = manuf.MacParser(update=True)
    vendor = p.get_all(mac).manuf
    # delete the downloaded database to cleanup after ourselves
    os.unlink('manuf')
    return vendor