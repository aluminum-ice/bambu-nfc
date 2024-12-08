
import codecs, binascii, sys, struct

def n_split_string(s:str, n:int) -> str:
    # split the string into n characters
    return " ".join([s[i:i+n] for i in range(0, len(s), n)])

def hex_to_float_le(hex_str) -> float:
    """Converts a hexadecimal string representing a little-endian float to a float."""

    # Convert the hex string to bytes
    hex_bytes = bytes.fromhex(hex_str)

    # Unpack the bytes as a little-endian float
    return struct.unpack('<f', hex_bytes)[0]

def hex_to_int16_le(hex_str:str) -> int:
    hex_str = binascii.unhexlify(hex_str)
    return int.from_bytes(hex_str, byteorder=sys.byteorder)

def hex_to_string(hex_str:str) -> str:
    return codecs.decode(hex_str, 'hex').decode('utf-8').rstrip('\x00')