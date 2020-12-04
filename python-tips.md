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

### creating an executable file

If you want to create an executable it is first advisable to include a checksum in the code to ensure when the file is run, it ensures that the most recent release is being used.

The library required to then create the executable is pyinstaller which can be installed using the command line

```
pip install pyinstaller
```

You can then use the command line to navigate to the directory containing your code and run the installer:

```
C: # Or other drive if your code is stored elsewhere  (e.g. M:)
cd C:\Users\username\mycode # replace with the directory of your .py file
pyinstaller --onefile --console mycode.py # replace mycode.py with the filename of your script
```

onefile means that the executable will work as a single file without relying on other folders that will be created during the build.
console means that any print statements in your code will still be displayed in a command window pop up. 
more comprehensive documentation can be found here: https://pyinstaller.readthedocs.io/en/stable/usage.html

I recommend adding a line at the end of your code to prevent it from automatically closing when it finishes running

```
input('The code has finished running, please press enter to close window:')
```

## checking your code for pep8 compliance

If you write code that abides by the rules set out by pep8 it makes it more readable and easier to work collaboratively
You can find out more about the pep8 style here:  [realpython.com/python-pep8/](https://realpython.com/python-pep8/)

https://realpython.com/python-pep8/

But a quick way to check if your code is compliant with most of the rules is to run the library 'pycodestyle'
You first need to install this library

```
pip install pycodestyle
```
You can then use the command line to navigate to the directory containing your code and run the installer:

```
C: # Or other drive if your code is stored elsewhere  (e.g. M:)
cd C:\Users\username\mycode # replace with the directory of your .py file
pycodestyle mycode.py # replace mycode.py with the filename of your script
```
this will then return blank if your code is compliant or print line by line deviations from pep8 style.
