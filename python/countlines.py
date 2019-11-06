import os
import glob

names={}

# Basic Python script to count number of lines in a folder
# Improvments are that it should be recursive and we can pass in multiple file types etc!
def count_lines(dir, files):
  os.chdir(dir)
  for fn in glob.glob('*.py'):
      with open(fn) as f:
          names[fn]=sum(1 for line in f if line.strip() and not line.startswith('#'))

count_lines('./yourdir', names)
count_lines('./anotherdir', names)

total_lines = sum(names.values())

print(names)
print("Total Lines {}".format(total_lines))