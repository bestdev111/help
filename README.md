# Help 'for all the things'

Here is a help file 'for all the things'. Good luck!
# Bash Alias

```
alias rs="bundle exec rails s"
alias rc="bundle exec rails c"
alias gs='git status '
alias ga='git add '
alias gb='git branch '
alias gc='git commit'
alias gd='git diff'
alias go='git checkout '
alias eh='subl ~/workspace/help/README.md'

export EDITOR=nano
export KOPS_STATE_STORE=s3://kops-state-rt7665
```

# Find and replace text docs
## example below replaces ugly with beautiful
`sed -i 's/ugly/beautiful/g' /home/bruno/old-friends/sue.txt`

## This example finds all files in cd and replaces 12345 with 54321
`find . -name *.orig -exec rm {} \; -o -name *DS_Store* -exec rm {} \;`

# Working with Files (find, rename, cat, tail, grep etc)
`rename 's/\.png$/.jpg/' *.png`	 # rename all .png to .jpg
`rename 's/^/avatar_/' *.png`		# append 'avatar_' to all .png files
`ls ~someuser/`	# Shortcut to the home directory of someuser
`ls /etc/*a.*` 	# Finds all files in /etc/ with a follwoed by .
`find . -name '*.xml'` 	# Will find all xml files recursive under the cd
`find ~ -name development.log` 		# Find all files with name development.log under the home(~)
`find ~ -name '*.txt' -perm 644`		# Finds all .txt files with permission 644
`find ~ -mtime 0`						# Finds all files modified in the last 24 hours (0 = 24hrs, 1 = 48hrs, 2 = 72hrs)
`find ~ -atime 0`						# Finds all files accessed in the last 24 hours (0 = 24hrs, 1 = 48hrs, 2 = 72hrs)
`find workspace -amin 1`				# Finds all files accessed in the last 1 minute (can also use: amin, cmin, mmin)
`find workspace -name dadou -exec rm '{}' \;`	# Finds and deletes all found (test the find on it's own first!)
`find workspace -name CVS -type d -exec rm -r '{}' \;`	# Finds and recursive deletes all CVS folders under workspace
`find / -user darren`			- Finds all files by darren
`find / -user darren –exec grep root {} \;` # Finds all files by darren that contain the word "root" (note the use of -exec and "\;" at the end)
`find ~/workspace -type f -empty` # Find all empty files
`find ~/workspace -type d -empty` # Find all empty folders
`tac` 	# 'cat' command in reverse! It dumps content of file in reverse
`tail` 	- shows the last 10 lines of a file
`tail -40 /etc/sometime.txt`	# Dumps last 40 lines of sometime.txt
`tail –f`	- shows the last lines of a file and adds to the output as the file grows
`grep -r dadou ./workspace/*`  # Find everything in the workspace that contains the word dadou in the file 
`ls -l > list_of_files.txt` #Redirects the output to a file
`ls -l >> list_of_files.txt` # Redirects the output to a file (and appends the contents >>)
`cp -r /var/lib/ejabberd/ workspace/backup/` 	#Copy a folder from one location to another (note -r)
`ln -s jruby-1.4.0/ jruby` # creates a simlink to the install folder for JRuby

# Clean VPN route if connection fails
1st turn off wifi manually
`sudo route flush`