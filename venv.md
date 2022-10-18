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
