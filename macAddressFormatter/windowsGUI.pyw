#! python

import tkinter as tk
from mac_format_module import change_mac_address_format


def main():

    def submitAction():
        oldMacs = macsToConvertBox.get(1.0, 'end-1c').split('\n')
        newMacs = []
        for mac in oldMacs:
            if macFormat.get() == 1:
                newMacs.append(
                    change_mac_address_format(
                        mac, '000000000000'))
            elif macFormat.get() == 2:
                newMacs.append(
                    change_mac_address_format(
                        mac, '00:00:00:00:00:00'))
            elif macFormat.get() == 3:
                newMacs.append(
                    change_mac_address_format(
                        mac, '0000.0000.0000'))
            elif macFormat.get() == 4:
                newMacs.append(
                    change_mac_address_format(
                        mac, '000.000.000.000'))
            elif macFormat.get() == 5:
                newMacs.append(
                    change_mac_address_format(
                        mac, '00.00.00.00.00.00'))
            elif macFormat.get() == 6:
                newMacs.append(
                    change_mac_address_format(
                        mac, '0000:0000:0000'))
            elif macFormat.get() == 7:
                newMacs.append(
                    change_mac_address_format(
                        mac, '00-00-00-00-00-00'))
            elif macFormat.get() == 8:
                newMacs.append(
                    change_mac_address_format(
                        mac, '0000-0000-0000'))
            else:
                newMacs.append('%s is not in a support format.' % mac)

        convertedMacsBox.delete(0.0, tk.END)
        convertedMacsBox.insert(tk.END, '\n'.join(newMacs))

    root = tk.Tk()  # Create the root window
    macFormat = tk.IntVar()
    root.title('MAC Address Formatter')  # Set the root window name
    root.configure(background='black')  # Set background color

    # Create the welcome message
    welcomeMessage = '''Welcome!
1. Paste Macs into the box on left
2. Click your desired format
3. Converted MAC addresses appear on the right.\n'''

    # Create the welcome label
    welcomeLabel = tk.Label(root,
                            text=welcomeMessage,
                            fg='white',
                            bg='black')

    # Create the label that will point to input box
    inputLabel = tk.Label(root,
                          text='Macs to Convert:',
                          fg='white',
                          bg='black')

    # Create the label that will point to output box
    outputLabel = tk.Label(root,
                           text='Converted Macs:',
                           fg='white',
                           bg='black')

    formatLabel = tk.Label(root,
                           text='\nSelect desired format:',
                           fg='white',
                           bg='black')

    # Create input text box
    macsToConvertBox = tk.Text(root, width=20, height=10, bg='white')

    # Create output text box
    convertedMacsBox = tk.Text(root, width=20, height=10, bg='white')

    # This button will clear the input text box
    inputClearButton = tk.Button(root,
                                 text='CLEAR',
                                 width=6,
                                 command=lambda: macsToConvertBox.delete(
                                     0.0, tk.END))

    # This button will clear the output text box
    outputClearButton = tk.Button(root,
                                  text='CLEAR',
                                  width=6,
                                  command=lambda: convertedMacsBox.delete(
                                      0.0, tk.END))

    # Place all the above objects into the GUI
    welcomeLabel.grid(row=0, column=0, columnspan=2)
    inputLabel.grid(row=1, column=0, sticky=tk.W)
    outputLabel.grid(row=1, column=1, sticky=tk.E)
    formatLabel.grid(row=4, column=0, columnspan=2)
    macsToConvertBox.grid(row=2, column=0, sticky=tk.W)
    convertedMacsBox.grid(row=2, column=1, sticky=tk.E)
    inputClearButton.grid(row=3, column=0, sticky=tk.W)
    outputClearButton.grid(row=3, column=1, sticky=tk.E)

    # Create Radio Buttons

    macOptions = {
        "000000000000": 1,
        "00:00:00:00:00:00": 2,
        "0000.0000.0000": 3,
        "000.000.000.000": 4,
        "00.00.00.00.00.00": 5,
        "0000:0000:0000": 6,
        "00-00-00-00-00-00": 7,
        "0000-0000-0000": 8}

    for mac, val in macOptions.items():
        tk.Radiobutton(root,
                       text=mac,
                       indicatoron=0,
                       width=20,
                       padx=20,
                       variable=macFormat,
                       command=submitAction,
                       value=val).grid(row=4+val, column=0, columnspan=2)
    root.mainloop()  # Open the GUI


if __name__ == '__main__':
    main()
