Designed based on guide outlined on [makeareadme.com](https://www.makeareadme.com/) but with some personal additions.

--------------------------------------------------------------------------------

# TITLE

Brief description of the package/programme etc.

_BADGES_ - can add badges of metadata such as version info ([shields.io](https://shields.io/) gives many good options).

## Components

If formed of multiple parts, outline file structure

## Installation

Clone this repo from github:

```console
git clone https://github.com/UCLHp/[repo name].git
```

Create an environment in which the code will run (these instructions use the basic python environment builder included with most Python installs). Open a command terminal and type the following  (you can exclude the parts in `[ ]` for directory paths if you are in the repo directory):

```console
cd <path to github repo>/[repo name]
mkdir env
python -m venv [<path to github repo>/[repo name]/]env/
```

This creates the environment. To activate the environment either use `activate.bat` on Windows or source `activate` on Linux/Mac

```console
##  Windows
[<path to github repo>/[repo name]/]env/Scripts/activate.bat
##  Linux/Mac
source [<path to github repo>/[repo name]/]env/Scripts/activate
```

Install the required packages as instructed in the **Requirements** section below.

To deactivate the virtual environment, simply type `deactivate`, and to remove the virtual environment delete the folder `env`.

### Requirements

The following dependency packages will need to be installed. They are as listed in the `requirements.txt` file within this package.<br>
To install from `requirements.txt`, within your environment, navigate back to `<path to github repo>/[repo name]` and run the following command:

```python
python -m pip install -r requirements.txt
```

`requirements.txt`:

```python
package==x.xx.x
```

### Tests

Included tests, how to use them, what results to expect

## Usage

How to use the package.

## Limitations / Known Bugs

Anything you know doesn't work

## Contribute

Pull requests are welcome.<br>
For major changes, please open a ticket first to discuss desired changes: [[repo name]/issues](http://github.com/agosling/[repo name]/issues)

If making changes, please check all tests and add if required.

## Licence

All code within this package distributed under [GNU GPL-3.0 (or higher)](https://opensource.org/licenses/GPL-3.0).

Full license text contained within the file LICENCE.

### (C) License for all programmes

```
###  Copyright (C) 2021:  Andrew J. Gosling

  #  This program is free software: you can redistribute it and/or modify
  #  it under the terms of the GNU General Public License as published by
  #  the Free Software Foundation, either version 3 of the License, or
  #  (at your option) any later version.

  #  This program is distributed in the hope that it will be useful,
  #  but WITHOUT ANY WARRANTY; without even the implied warranty of
  #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  #  GNU General Public License for more details.

  #  You should have received a copy of the GNU General Public License
  #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
