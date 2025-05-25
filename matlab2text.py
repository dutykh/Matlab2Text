#!/usr/bin/env python3
# =============================================================================
#  matlab2text.py
#  Concatenate all Matlab .m files in the current directory into a single .txt file.
#
#  Author: Dr Denys Dutykh (Khalifa University of Science and Technology, Abu Dhabi, UAE)
#
#  License: GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
#  See: https://www.gnu.org/licenses/gpl-3.0.html
# =============================================================================
"""
matlab2text.py: Concatenate all Matlab .m files in the current directory (and optionally subdirectories) into a single .txt file.

Usage:
  python3 matlab2text.py outputname
  python3 matlab2text.py outputname.txt
  python3 matlab2text.py -r outputname
  python3 matlab2text.py outputname.txt -r

Options:
  -h, --h, -hep, --help   Show this help message and exit.
  -r                      Recursively search subdirectories for .m files.
"""

import sys
import glob

HELP_TEXT = """
matlab2text.py: Concatenate all Matlab .m files in the current directory (and optionally subdirectories) into a single .txt file.

Usage:
  python3 matlab2text.py outputname
  python3 matlab2text.py outputname.txt
  python3 matlab2text.py -r outputname
  python3 matlab2text.py outputname.txt -r

Options:
  -h, --h, -hep, --help   Show this help message and exit.
  -r                      Recursively search subdirectories for .m files.

Examples:
  python3 matlab2text.py outputname.txt -r

Options:
  -h, --h, -hep, --help   Show this help message and exit.
  -r                      Recursively search subdirectories for .m files.
"""

HELP_FLAGS = {"-h", "--h", "-hep", "--help"}


def show_help():
    print(HELP_TEXT)
    sys.exit(0)


def main():
    # If called with help flags, show help
    args = [arg for arg in sys.argv[1:] if arg not in HELP_FLAGS]
    if len(sys.argv) >= 2 and any(arg in HELP_FLAGS for arg in sys.argv[1:]):
        show_help()

    recursive = "-r" in sys.argv[1:]
    args = [arg for arg in sys.argv[1:] if arg != "-r"]

    # Determine output filename
    if len(args) == 0:
        outname = "matlabsources.txt"
    elif len(args) == 1:
        outname = args[0]
        if not outname.lower().endswith(".txt"):
            outname += ".txt"
    else:
        show_help()

    # Find .m files
    if recursive:
        m_files = sorted(glob.glob("**/*.m", recursive=True))
    else:
        m_files = sorted(glob.glob("*.m"))
    if not m_files:
        print("No .m files found in the specified location.")
        sys.exit(1)

    with open(outname, "w", encoding="utf-8") as outfile:
        for fname in m_files:
            outfile.write(f"=== Start file: {fname} ===\n\n")
            with open(fname, "r", encoding="utf-8", errors="replace") as infile:
                outfile.write(infile.read())
                outfile.write("\n")
            outfile.write(f"\n=== End file {fname} ===\n\n")
    print(f"Concatenated {len(m_files)} files into {outname}.")


if __name__ == "__main__":
    main()
