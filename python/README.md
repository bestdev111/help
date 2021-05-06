## Python2 HTTP Server

`python -m SimpleHTTPServer`

## Python3 HTTP Server

`python3 -m http.server`

## PIP

Install a Python pip package directly from Github:

```
# For example, install the master branch HEAD fof vcrpy package:
pip uninstall vcrpy
pip install https://github.com/kevin1024/vcrpy/archive/master.zip
```

## Python Environments

```
# Create a new venv called venv
python -m venv venv

# Activate the venv environment
source venv/bin/activate

# Deactivate the environment
deactivate
```

## Get date from timestamp

```
import datetime
timestamp = 1618445100
date = datetime.datetime.fromtimestamp(1618445100)
print(date.strftime('%Y-%m-%d %H:%M:%S'))

# 2021-04-15 07:05:00
```

## Jupyter Notebook

This section assumes you have already instaled [Anaconda](https://www.anaconda.com/products/individual).

Start a notebook server from a specific folder:

```
cd mynotebooks
jupyter notebook
```

### NBConvert

Convert a notebook a differnet file format using `nbconvert`

```
jupyter nbconvert --to html working-with-code-cells.ipynb
```

More details in the [Nbconvert Docs](https://nbconvert.readthedocs.io/en/latest/usage.html).

### Magic Keywords

NOTE: To list all available magic keywords using `%lsmagic` and run that cell in a notebook.

Some of the most popular [magic commands are listed here](https://towardsdatascience.com/top-8-magic-commands-in-jupyter-notebook-c1582e813560).

Run the Python debugger using `%pdb`

Time a function using ``