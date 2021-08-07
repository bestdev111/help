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

### Slideshows

You can create a slideshow from a Jupyter notebook.

First select the notebook type under `View -> Cell Toolbar -> Slideshow`.

Now, each cell can choose the type of slide that it is.

Slides are full slides that you move through left to right. Sub-slides show up in the slideshow by pressing up or down. Fragments are hidden at first, then appear with a button press. You can skip cells in the slideshow with Skip and Notes leaves the cell as speaker notes.

Here is an [example of a slideshow in a Jupyter Notebook](https://github.com/jorisvandenbossche/2015-PyDataParis/blob/master/pandas_introduction.ipynb).

### Create a link to download a dataframe from a Notebook

Lets say you have access to a Pandas DataFrame `df` in your notebook but do not have the original file or the data in a file format at all. In this case you can save the file using `to_csv` function and use the `FileLink` module to display a link in the Jupyter Notebook to download it like so:

```
from IPython.display import FileLink
df.to_csv('mydf.csv', index=False)
display(FileLink('mydf.csv'))
```

You can also use this utility to copy a private folder to another location in a public workspace:

```
import shutil
shutil.copytree('../../data/project_1/', '/home/workspace/data')
```

### Lists

```
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', "Dec"]
q3 = months[6:9] #start index is inclusive , end index is exclusive
print(q3) # ['Jul', 'Aug', 'Sep']

first_half = months[:6]
print(first_half) # ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

second_half = months[6:]
print(second_half) # ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fishes = "one fish, two fish, red fish, blue fish"
print(fishes.count('fish')) # 4

print('fish' in  fishes) # True
print('Sun' in months) # False

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# Get the last three eclipse dates: (two possible solutions!)
print(eclipse_dates[7:])
print(eclipse_dates[-3:]) # here the start index is 3 in then go to the end


sentence = ["I", "wish", "to", "register", "a", "complaint", "."]
sentence2[0:2] = ["We", "want"] #  replaces element 0 and 1 with this

numbers = [5,2,4,3,1]
min(numbers) # 1
max(numbers) # 5
sorted(numbers) # [1,2,3,4,5]

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) # True
print(a is b) # True ('is' here same as '===' in javascript)
print(a == c) # True
print(a is c) # False
```

### Strings

**Interpolation**

```
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

print(f"{username} accessed the site {url} at {timestamp}") # Kinari accessed the site http://petshop.com/pets/mammals/cats at 04:50
```

**Format**

```
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))
```

**join**

```
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

name = "-".join(["García", "O'Kelly"])
print(name)
```

### Tuples

```
AngkorWat = (13.4125, 103.866667)
print(type(AngkorWat))
lat, lon = AngkorWat # Tuple unpacking
print(lat)
```


### Sets

```
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a) # {1, 2, 3, 4}
b.pop()
print(b) # {2, 3, 4}
```

### Dictionary

```
population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
population['Shanghai'] # 17.8
population.get('London') # None
population.get('Vulcan', 'City not found') # 'City not found'
```

### If, then else

```
season = 'spring'
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")
```

### Loops

**for loops**

To simply loop use the iterable property like so:

```
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
```

To modify a list in place using the index then use `range` with `len` like so:

```
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()
```

Another example: create username from a list of full names:

```
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ','_'))

print(usernames)
```

Yet another example: create a HTML list:

```
items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)
```

Using a dictionary with the get method to check for words and updating a word counter:

```
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {}

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter) # {'huckleberry': 1, 'gasby': 1, 'sherlock': 1, 'hamlet': 1, 'expectations': 1, 'fin': 1, 'of': 2, 'great': 2, 'adventures': 2, 'the': 2, 'holmes': 1}
```

**range**

A quick note on range (which is defined as `range(start=0, stop, step=1)`):

```
range(4) # 0, 1, 2, 3
range(2, 6) # 2, 3, 4, 5
range(1, 10, 2) # 1, 3, 5, 7, 9
```

Note to actually print these out use, for example: `print(list(range(4))) # [0, 1, 2, 3]`