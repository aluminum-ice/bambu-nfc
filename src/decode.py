#! /usr/bin/env python3

import argparse
from datetime import datetime

from utils.helper import hex_to_float_le, hex_to_int16_le, hex_to_string

def filament_type(block: str) -> str:
	return hex_to_string(block.replace(" ", ""))

def detailed_filament_type(block: str) -> str:
	return hex_to_string(block.replace(" ", ""))

def filament_color(block: str) -> str:
	hex_str = block.split(' ')[:4]
	return "#" + "".join(hex_str)

def spool_weight(block: str) -> str:
	hex_str = "".join(block.split(' ')[4:6])
	return hex_to_int16_le(hex_str)

def filament_diameter(block: str) -> str:
	hex_str = "".join(block.split(' ')[8:12])
	return hex_to_float_le(hex_str)

def filament_drying_temperature(block: str) -> str:
	hex_str = "".join(block.split(' ')[:2])
	return hex_to_int16_le(hex_str)

def filament_drying_time(block: str) -> str:
	hex_str = "".join(block.split(' ')[2:4])
	return hex_to_int16_le(hex_str)

def filament_bed_temperature(block: str) -> str:
	hex_str = "".join(block.split(' ')[6:8])
	return hex_to_int16_le(hex_str)

def max_hotend_temperature(block: str) -> str:
	hex_str = "".join(block.split(' ')[8:10])
	return hex_to_int16_le(hex_str)

def min_hotend_temperature(block: str) -> str:
	hex_str = "".join(block.split(' ')[10:12])
	return hex_to_int16_le(hex_str)

def spool_width(block: str) -> str:
	hex_str = "".join(block.split(' ')[4:6])
	return hex_to_int16_le(hex_str)/100

def production_datetime(block: str) -> str:
	pd = datetime.strptime(hex_to_string(block.replace(" ", "")), '%Y_%m_%d_%H_%M')
	return pd.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':

	encoded = {}
	with open('../nfc/PLA//PLA_BASIC_GREEN_1.nfc', 'r') as file:
	    # Read each line in the file
	    for line in file:
	        s = line.strip().split(':')
	        if len(s) > 1:
	        	k, v = s
	        	encoded[k.strip()] = v.strip()

	decoded = {}

	decoded["type"] = filament_type(encoded["Block 2"])
	decoded["detailed type"] = detailed_filament_type(encoded["Block 4"])
	decoded["color"] = filament_color(encoded["Block 5"])
	decoded["diameter [mm]"] = filament_diameter(encoded["Block 5"])
	decoded["spool weight [g]"] = spool_weight(encoded["Block 5"])
	decoded["drying temperature [C]"] = filament_drying_temperature(encoded["Block 6"])
	decoded["drying time [H]"] = filament_drying_time(encoded["Block 6"])
	decoded["bed temperature [C]"] = filament_bed_temperature(encoded["Block 6"])
	decoded["max hotend temperature [C]"] = max_hotend_temperature(encoded["Block 6"])
	decoded["min hotend temperature [C]"] = min_hotend_temperature(encoded["Block 6"])
	decoded["spool width [mm]"] = spool_width(encoded["Block 10"])
	decoded["production datetime"] = production_datetime(encoded["Block 12"])

	print(decoded)



    # parser = init_argparse()
    # args = parser.parse_args()

    # keys = kdf(uid_bytes(args.uid))

    # if args.filename is None:
    #     if args.flipper == False:
    #         print([a.hex().upper() for a in keys])
    #     else:
    #         for a in keys:
    #             print(a.hex().upper())

    # if args.filename is not None:
    #     to_json_file(args.uid, keys, args.filename)