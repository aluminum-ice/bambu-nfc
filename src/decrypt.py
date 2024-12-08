#! /usr/bin/env python3

import argparse, os, json
from Cryptodome.Protocol.KDF import HKDF
from Cryptodome.Hash import SHA256

from utils.parser import init_argparse

def n_split_string(s:str, n:int) -> str:
    # split the string into n characters
    return " ".join([s[i:i+n] for i in range(0, len(s), n)])

def uid_bytes(value:str) -> bytes:
    
    uid = n_split_string(value, 2).split(' ')
    uid = list(map(lambda v: int(v, 16), uid))

    # convert int list into bytes
    return bytes(uid)

def kdf(uid:bytes) -> str:

    master = bytes([0x9a,0x75,0x9c,0xf2,0xc4,0xf7,0xca,0xff,0x22,0x2c,0xb9,0x76,0x9b,0x41,0xbc,0x96]) 

    # generate the keys
    keys=HKDF(uid, 6, master, SHA256, 16, context=b"RFID-A\0")

    return keys

def to_json_file(uid:str, keys:str, filename:str):

    n = 2
    # split the string 
    uid = [uid[i:i+n] for i in range(0, len(uid), n)]

    data = {}
    data["UID"] = " ".join(uid)

    block = {}
    for i, k in enumerate(keys):
        block["Block " + str(4*i + 3)] = n_split_string(k.hex().upper(),2)

    data["A-KEY"] = block

    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':

    parser = init_argparse()
    args = parser.parse_args()

    keys = kdf(uid_bytes(args.uid))

    if args.filename is None:
        if args.flipper == False:
            print([a.hex().upper() for a in keys])
        else:
            for a in keys:
                print(a.hex().upper())

    if args.filename is not None:
        to_json_file(args.uid, keys, args.filename)

