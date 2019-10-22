# Hints and Tips for Python


### creating a package in a folder

If you want to have a folder in which you have many different python programmes that you want to be able to call externally, the following tips should hopefully help:

To add the folder to the list of places that python will search for programmes that it will import, use the following code at the start of your python programme:
```
from os import path as osPath  
from sys import path as sysPath  
sysPath.append(osPath.join(osPath.split(sysPath[0])[0],'packages'))
```
Within this folder (or sub-folders) you can then create as many files as you like containing functions and classes that you have created, either one function to a file, or collections of functions in separate files.

You can then read in any of the functions that you have defined within the programmes using the line
```
from [folder].[filename] import [function]
```

.

For increased functionality, within the folder containing all of your own programmes, create a file called:  `__init__.py`  
Add all of your `from [folder].[filename] import [function]` lines into this file  
You can then import a specific function as (acting much more as publicly available packages do)
```
from [folder] import [function]
```

.

This gives a more comprehensive summary:  https://stackoverflow.com/questions/598668/external-classes-in-python
