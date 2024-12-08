#! /usr/bin/env python3

import argparse, json
from datetime import datetime

from utils.helper import hex_to_float_le, hex_to_int16_le, hex_to_string
from utils.parser import decode_argparse

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

def filament_length(block: str) -> str:
    hex_str = "".join(block.split(' ')[4:6])
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

def read_nfc_file(filename: str) -> dict:
    encoded = {}
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            s = line.strip().split(':')
            if len(s) > 1:
                k, v = s
                encoded[k.strip()] = v.strip()

    return encoded


if __name__ == '__main__':

    parser = decode_argparse()
    args = parser.parse_args()

    encoded = read_nfc_file(args.nfc)

    data = {}
    data["file"] = args.nfc

    filament = {}
    filament["type"] = filament_type(encoded["Block 2"])
    filament["detailed type"] = detailed_filament_type(encoded["Block 4"])
    filament["color"] = filament_color(encoded["Block 5"])
    filament["diameter [mm]"] = filament_diameter(encoded["Block 5"])
    filament["length [m]"] = filament_length(encoded["Block 14"])
    filament["drying temperature [C]"] = filament_drying_temperature(encoded["Block 6"])
    filament["drying time [H]"] = filament_drying_time(encoded["Block 6"])
    data["filament"] = filament

    spool = {}
    spool["weight [g]"] = spool_weight(encoded["Block 5"])
    spool["width [mm]"] = spool_width(encoded["Block 10"])
    data["spool"] = spool

    printing = {}


    printing["bed temperature [C]"] = filament_bed_temperature(encoded["Block 6"])
    printing["min hotend temperature [C]"] = min_hotend_temperature(encoded["Block 6"])
    printing["max hotend temperature [C]"] = max_hotend_temperature(encoded["Block 6"])
    data["print"] = printing

    data["production datetime"] = production_datetime(encoded["Block 12"])

    if args.filename is not None:
        with open(args.filename, 'w') as f:
            json.dump(data, f)
    else:
        print(data)
