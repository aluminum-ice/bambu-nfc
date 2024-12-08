#! /usr/bin/env python3

import argparse, codecs

encoded = {}
with open('../nfc/PLA//PLA_BASIC_GREEN_1.nfc', 'r') as file:
    # Read each line in the file
    for line in file:
        s = line.strip().split(':')
        if len(s) > 1:
        	k, v = s
        	encoded[k.strip()] = v.strip()

# print(data)


decoded = {}

decoded["Filament Type"] = codecs.decode(encoded["Block 2"].replace(" ", ""), 'hex').decode('utf-8').rstrip('\x00')
decoded["Detailed Filament Type"] = codecs.decode(encoded["Block 4"].replace(" ", ""), 'hex').decode('utf-8').rstrip('\x00')


print(decoded)