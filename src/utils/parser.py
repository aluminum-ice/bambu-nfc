import argparse


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] ...", description="generate encryption keys for bambu nfc tags using the tag's uid written as a string (e.g., 6AA42B72)"
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} version 0.0.1"
    )
    parser.add_argument(
        "-u",
        "--uid",
        action="store",
        help="uid (default: %(default)s)",
        type=str,
        required=True,
        default=None,
    )
    parser.add_argument(
        "-f",
        "--filename",
        action="store",
        help="optional output file name (default: %(default)s)",
        type=str,
        nargs='?', 
        const="keys.json",
        required=False,
    )
    parser.add_argument(
        "--flipper",
        action=argparse.BooleanOptionalAction,
        help="output in flipper friendly format (default: %(default)s)",
        required=False,
        default=False,
    )


    return parser
