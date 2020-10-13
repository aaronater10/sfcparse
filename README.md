# sfconfig Module for Python
##### sfconfig = Simple File Configuration
##### Current Version 0.6.3

This module allows you to easily import, export, and append configuration data for your python program or script
in any plain text file with any file extension. ** It can be used to easily export any string data to a file as well **.

##### Goal for the Project:
To provide an easy alternative to using .ini files in an attempt to make importing python data and saving any data to files for your projects simple. This also gives you the universal freedom to use any file extension or any made up file type you want.
___
##### Importing (Python only):
Imports stored variable names and their assigned values from any text file.

Returns a class with attributes from the file keeping python's natural recognition of data types, including comment lines being ignored.

###### Accepted Imported Data Types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes
___
##### Exporting/Appending:
It simply sends string data to a file. It may be used for any string data file output.
___

# Tutorial
Coming soon.

# Tutorial Video
Coming soon.
___
# Module Performance
Coming soon.
___

# Known Limitations
Importing
 - Does not support importing unpacked variables and values
 - Does not support importing values with a variable stored inside
 - Does not ignore comments at the end of a value imported

# Future Upgrades
Importing
- Add support for importing values with variables inside
- Add support for unpacked variables and values
- Add ability to ignore comments at end of a value
- Add ability to have Sections like a .ini file
