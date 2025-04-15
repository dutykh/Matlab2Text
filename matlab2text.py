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
matlab2text.py: Concatenate all Matlab .m files in the current directory into a single .txt file.

Usage:
  python3 matlab2text.py outputname
  python3 matlab2text.py outputname.txt

Options:
  -h, --h, -hep, --help   Show this help message and exit.
"""
import os
import sys
import glob

HELP_TEXT = """
matlab2text.py: Concatenate all Matlab .m files in the current directory into a single .txt file.

Usage:
  python3 matlab2text.py outputname
  python3 matlab2text.py outputname.txt

Options:
  -h, --h, -hep, --help   Show this help message and exit.
"""

HELP_FLAGS = {'-h', '--h', '-hep', '--help'}

def show_help():
    print(HELP_TEXT)
    sys.exit(0)

def main():
    # If called with help flags, show help
    if len(sys.argv) == 2 and sys.argv[1] in HELP_FLAGS:
        show_help()
    # If called with no arguments, use default output filename
    if len(sys.argv) == 1:
        outname = 'matlabsources.txt'
    # If called with one argument (not help), use that as output filename
    elif len(sys.argv) == 2:
        outname = sys.argv[1]
        if not outname.lower().endswith('.txt'):
            outname += '.txt'
    else:
        show_help()

    m_files = sorted(glob.glob('*.m'))
    if not m_files:
        print("No .m files found in the current directory.")
        sys.exit(1)

    with open(outname, 'w', encoding='utf-8') as outfile:
        for fname in m_files:
            outfile.write(f"=== Start file: {fname} ===\n\n")
            with open(fname, 'r', encoding='utf-8', errors='replace') as infile:
                outfile.write(infile.read())
                outfile.write('\n')
            outfile.write(f"\n=== End file {fname} ===\n\n")
    print(f"Concatenated {len(m_files)} files into {outname}.")

if __name__ == '__main__':
    main()
