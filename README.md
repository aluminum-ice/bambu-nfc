# bambu-nfc

This repository stores 1) Bambu NFC tag data read using a Flipper Zero (e.g., `/nfc/PLA`); 2) Python code that can generate the A-Keys for the Bambu tag (e.g., `/src/gen_key.py`); and 3) Python code that can decode the Bambu NFC tag data into a human readable JSON file.

The `/decoded` directory provides sample human readable JSON files generated from the NFC files in the `/nfc` directory.

## gen_key.py

`python3 ./decrypt.py -u 6AA42B72 -f ../nfc/ABS/ABS-GF_ORANGE_1.json`

See `python3 ./gen_key.py -h` for information on input arguments. 

## decode.py

`./decode.py -n ../nfc/PLA/PLA_BASIC_GREEN_1.nfc -f ../decoded/PLA_Basic.json`

See `python3 ./decode.py -h` for information on input arguments. 
```
{
    "file": "../nfc/PLA/PLA_BASIC_GREEN_1.nfc",
    "filament": {
        "type": "PLA",
        "detailed type": "PLA Basic",
        "color": "#00AE42FF",
        "diameter [mm]": 1.75,
        "length [m]": 82,
        "drying temperature [C]": 55,
        "drying time [H]": 8
    },
    "spool": {
        "weight [g]": 250,
        "width [mm]": 66.25
    },
    "print": {
        "bed temperature [C]": 0,
        "min hotend temperature [C]": 190,
        "max hotend temperature [C]": 230
    },
    "production datetime": "2024-04-30 13:44:00"
}
```
