#! /usr/bin/python3
from distutils.core import setup

setup(
    name='macAddressFormatter',
    version='2.0dev',
    author='Tony Clemons',
    author_email='clemons745@gmail.com',
    description='A simple mac address formatter',
    packages=['macAddressFormatter'],
    license='GNU General Public License v3 (GPLv3)',
    long_description=open('readme.txt').read(),
    keywords='mac address format formatter media access control',
    url="https://github.com/clemons745/mac_address_formatter",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Environment :: Console',
        'Environment :: Win32 (MS Windows)'
    ],
)
