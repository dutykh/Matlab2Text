# Matlab2Text Utility

## Overview

**matlab2text.py** is a simple Python utility that scans the current directory for all Matlab source files (`*.m`) and concatenates them into a single text file. This is particularly useful for preparing Matlab code for submission to Large Language Models (LLMs) like ChatGPT, Gemini, etc., which may not accept `.m` files directly.

- **Author:** Dr Denys Dutykh (Khalifa University of Science and Technology, Abu Dhabi, UAE)
- **License:** GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007

---

## Features

- Scans the current directory for all `.m` files
- Concatenates their contents into a single `.txt` file
- Output filename is provided as the first command-line argument (with or without `.txt` extension; `.txt` is auto-added if needed)
- Each file's content is delimited with clear start/end markers:

  ```
  === Start file: filename.m ===
  ...file contents...
  === End file filename.m ===
  ```
- Provides a help page for `-h`, `--h`, `-hep`, and `--help`

---

## Usage

From the command line, you can run the script in several ways:

- **No arguments:**

  ```sh
  python3 matlab2text.py
  ```
  This will create `matlabsources.txt` containing all `.m` files concatenated (default behavior).

- **With a custom output name:**

  ```sh
  python3 matlab2text.py outputname
  ```
  This will create `outputname.txt` containing all `.m` files concatenated.

- **With a custom output name and extension:**

  ```sh
  python3 matlab2text.py outputname.txt
  ```
  This will create `outputname.txt` containing all `.m` files concatenated.

To show the help page:

```sh
python3 matlab2text.py -h
python3 matlab2text.py --h
python3 matlab2text.py -hep
python3 matlab2text.py --help
```

---

## Example

Suppose your directory contains:
- `foo.m`
- `bar.m`

Running:
```sh
python3 matlab2text.py all_sources
```
will produce `all_sources.txt` with contents like:

```
=== Start file: bar.m ===
...contents of bar.m...
=== End file bar.m ===

=== Start file: foo.m ===
...contents of foo.m...
=== End file foo.m ===
```

---

## License

This utility is licensed under the GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007. See the `LICENSE` file or [the official GPLv3 page](https://www.gnu.org/licenses/gpl-3.0.html) for details.
