CONTENTS

1. INTRODUCTION

2. REQUIREMENTS

3. INSTRUCTIONS

4. SUPPORTTED MAC ADDRESS FORMATS

########################################################################

1. INTRODUCTION

This is a simple script that will take a list of mac addresses in a file, 1 per line, and change their format to a different format specified by the user.


2. REQUIREMENTS

If you would like to use the fetchMacVendor function, you will need to the manuf module.
This function is not used in the main script, and no other dependencies are required.

3. INSTRUCTIONS

Create a file with a list of mac address that you would like to convert the format of, one per line.  As long as the format is supported, it does not matter what format they are in.
Then supply filename as an argument when running the script.  For example:

macAddressFormatter.py macAddressList.txt

4. SUPPORTTED MAC ADDRESS FORMATS

000000000000
00.00.00.00.00.00
0000.0000.0000
000.000.000.000
00:00:00:00:00:00
0000:0000:0000
00-00-00-00-00-00
0000-0000-0000