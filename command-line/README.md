# Command Line

`sudo su` elevate to sudo user permanently (without password)

`du -skh *` check the size of files and folders in the current directory

`sed -i -e 's/"Amazon"/"Postgres"/g' appsettings.json` * find and replace a value in a file

`dpkg -l libgdiplus` * check if the libgdiplus is installed on the server

`host myip.opendns.com resolver1.opendns.com` *displays your public ip address*

`sed -i 's/ugly/beautiful/g' /home/bruno/old-friends/sue.txt`

`find . -name *.orig -exec rm {} \; -o -name *DS_Store* -exec rm {} \;`

`rename 's/\.png$/.jpg/' *.png`	*rename all .png to .jpg*

`rename 's/^/avatar_/' *.png`	*append 'avatar_' to all .png files*

`ls ~someuser/`	*Shortcut to the home directory of someuser*

`ls /etc/*a.*` 	*Finds all files in /etc/ with a follwoed by*

`find . -name '*.xml'` *Will find all xml files recursive under the cd*

`find ~ -name development.log` 	*Find all files with name development.log under the home(~)*

`find ~ -name '*.txt' -perm 644` *Finds all .txt files with permission 644*

`find ~ -mtime 0`	*Finds all files modified in the last 24 hours (0 = 24hrs, 1 = 48hrs, 2 = 72hrs)*

`find ~ -atime 0`	*Finds all files accessed in the last 24 hours (0 = 24hrs, 1 = 48hrs, 2 = 72hrs)*

`find workspace -amin 1` *Finds all files accessed in the last 1 minute (can also use: amin, cmin, mmin)*

`find workspace -name dadou -exec rm '{}' \;`	*Finds and deletes all found (test the find on it's own first!)*

`find workspace -name CVS -type d -exec rm -r '{}' \;` *Finds and recursive deletes all CVS folders under workspace*

`find / -user darren`	*Finds all files by darren*

`find / -user darren –exec grep root {} \;` *Finds all files by darren that contain the word "root" (note the use of -exec and "\;" at the end)*

`find ~/workspace -type f -empty` *Find all empty files*

`find ~/workspace -type d -empty` *Find all empty folders*

`find . -name "*.js" -exec bash -c 'mv "$1" "$(sed "s/\.js$/.ts/" <<< "$1")"' - '{}' \;` *Change all filenames of .js to .ts

`tac` *'cat' command in reverse! It dumps content of file in reverse*

`tail` 	*shows the last 10 lines of a file*

`tail -40 /etc/sometime.txt` *Dumps last 40 lines of sometime.txt*

`tail –f`	*shows the last lines of a file and adds to the output as the file grows*

`grep -r dadou ./workspace/*` *Find everything in the workspace that contains the word dadou in the file*

`ls -l > list_of_files.txt` *Redirects the STDOUT to a file*

`ls -l 2> list_of_files.txt` *Redirects the STDERR to a file*

`ls -l >> list_of_files.txt` *Redirects the output to a file (and appends the contents >>)*

See [Save Terminal Output to a File for details](https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file)

`cp -r /var/lib/ejabberd/ workspace/backup/` *Copy a folder from one location to another (note -r)*

`ln -s jruby-1.4.0/ jruby` *creates a simlink to the install folder for JRuby*

`ln -s /path/to/original /path/to/link` *a better example of creating a symlink*

`ln -s ../build/contracts vapp/contracts` *note the path of the original should be relative to the location of the link as shown.

`ln -s "/path/to/the original" /path/to/link` *example of creating a symlink if there are spaces in the directory (basically surround with quotes)*

`chmod a+wr /some/file` * enables /some/file to be read(r) and write(w) by all(a)

`chmod u+rw /some/file` * enables /some/file to be read(r) and write(w) by the owner(u)

`dig domain.com` * lookup dns records, mx records, nameservers, host ip, hosts etc

`nslookup mydomain.com` * alternaive dns info lookup

`dig -t MX rotati.tech` * lookup a specific DNS entry i.e. MX records

## Copy contents to clipboard

cat ~/.bashrc | pbcopy

## Get current version of Ubuntu

Use LSB Release

```
lsb_release -r
```

## Simple HTTP Server

Run a ruby WEBrick server from the command line:

```
ruby -run -e httpd .
```

## Start Brave in Incognito Mode from the command line

Helps with debugging and/or getting Brave to actaully start if it keeps crashing!

Solution found [here](https://community.brave.com/t/brave-crashes-constantly/101688/7).

```
open -a '/Applications/Brave Browser.app' --args --incognito
```

## Encode and Decode to / from Hexadecimal (Hex) - Base 16

```
# a string
xxd -p <<< "Blockchain Developer"
echo 426c6f636b636861696e20446576656c6f7065720a|xxd -r -p
# a text file
xxd -p hello.txt helloEncoded.txt
xxd -p -r helloEncoded.txt helloDecoded.txt
# an image
xxd -p cat.png cat.txt
xxd -p -r cat.txt catDecoded.png
```

## Check SHA Digest of a file download

```
shasum -a 256 filename
```

## Generate a random IOTA seed

**Using the mac terminal**

```
cat /dev/urandom |LC_ALL=C tr -dc 'A-Z9' | fold -w 81 | head -n 1
```

**Using a Python Script**

```
from random import SystemRandom
alphabet = u'9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
generator = SystemRandom()
print(u''.join(generator.choice(alphabet) for _ in range(81)))
```

** search in the terminal history

`CTL + r`