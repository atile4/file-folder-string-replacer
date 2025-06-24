# file-folder-string-replacer
Copies an inputted valid directory (and all of its contents) into a specified directory, and replaces all occurrences in directory name, file name, and file contents of a target string with a replacement string.

Directory inputs should contain the full path.

## Requirements
Python 3.4 Interpreter or above for shutil and pathlib modules

## Installation
1. Download main.py in the replacer folder
2. Run the file in a command line

## Example Usage
```SH
INPUT A DIRECTORY PATH: "C:\Users\attic\Desktop\foundations"
```

```SH
INPUT AN OUTPUT PATH: "C:\Users\attic\Desktop\output"
```

```SH
INPUT TARGET STRING: tpmt
INPUT REPLACEMENT STRING: REPLACED
INPUT FILE TYPE: sql
```
## Known Issues
- Inflexible directory path inputs 

- The program will only modify one type of a specified text file.

- Inputting a specified text file to modify is required rather than optional.
