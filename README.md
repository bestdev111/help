# Help 'for all the things'

Here is a help file 'for all the things'. Good luck!

By the way, here is a [markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

# Bash Alias

```
export EDITOR=nano
export KOPS_STATE_STORE=s3://kops-state-rt7665
export NAMESPACE=staging
eval "$(rbenv init -)"

alias rs="bundle exec rails s"
alias rc="bundle exec rails c"
alias gs='git status '
alias ga='git add '
alias gb='git branch '
alias gc='git commit'
alias gd='git diff'
alias go='git checkout '
alias eh='subl ~/workspace/help/README.md'
# alias ch='cd ~/workspace/help/;git add .;git commit -m \'Update help\';git push origin master'
alias ks='kubectl'
alias dc='docker-compose'
alias wk='cd ~/workspace/'
alias wkh='cd ~/workspace/help/'
dbash() { docker exec -it "$1" bash; }
ch() { cd ~/workspace/help/; git add .; git commit -m 'Update help'; git push origin master; }
```

# Terminal Tips!

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

`tac` *'cat' command in reverse! It dumps content of file in reverse*

`tail` 	*shows the last 10 lines of a file*

`tail -40 /etc/sometime.txt` *Dumps last 40 lines of sometime.txt*

`tail –f`	*shows the last lines of a file and adds to the output as the file grows*

`grep -r dadou ./workspace/*` *Find everything in the workspace that contains the word dadou in the file*

`ls -l > list_of_files.txt` *Redirects the output to a file*

`ls -l >> list_of_files.txt` *Redirects the output to a file (and appends the contents >>)*

`cp -r /var/lib/ejabberd/ workspace/backup/` *Copy a folder from one location to another (note -r)*

`ln -s jruby-1.4.0/ jruby` *creates a simlink to the install folder for JRuby*

`chmod a+wr /some/file` * enables /some/file to be read(r) and write(w) by all(a)

# Securly copy your SSH key to your clipboard

`pbcopy < ~/.ssh/id_rsa.pub`

## Docker & Docker Compose tips

A good image to use for playing around with Docker and Docker Compose is `tutum/hello-world`

NOTE 1 : If there is a `.env` file in the project directory then it's values will be picked up by compose.

NOTE 2: If there is a `docker-compose.override.yml` file in the same directory then running `docker-compose up` will merge the two files together to create a single config. The override file could be put into a .gitignore file thus allowing developers to make speciif local only changes there without causing issues with others.

`docker-compose exec <service-name> bash`

`docker network ls`

`docker network inspect <name>`

`docker inspect <container-name>`

`docker inspect --format '{{.LogPath}}' <container-name>`

`docker-compose logs -f`

`docker volumes ls`

`docker-compose config` #verifies the config is valid

## VPN (Tunnelblik)

1st turn off wifi manually then run:
`sudo route flush`

## Python HTTP Server

`python -m SimpleHTTPServer`

## Git

Change the username of the commit, run:

```
git config --global user.name "Darren Jensen"
git config --global user.email "darren.jensen@gmail.com"
git config credential.username 'jensendarren'
```