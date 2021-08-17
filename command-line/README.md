# Command Line

`sudo su` elevate to sudo user permanently (without password)

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

## Process managment

Use `pgrep` to get the process (PID) for a running application / process:

```
pgrep node
```

Use `pstree` to get the parent / child process tree for a PID:

```
pstree 126813

node─┬─node─┬─2*[node───6*[{node}]]
     │      └─42*[{node}]
     └─10*[{node}]
```

To expand the tree run with the `-s` switch:

```
pstree -ps  9317
systemd(1)───node(9317)─┬─{node}(9331)
                        ├─{node}(9332)
                        ├─{node}(9333)
                        ├─{node}(9334)
                        ├─{node}(9335)
                        ├─{node}(9337)
                        ├─{node}(9348)
                        ├─{node}(9349)
                        ├─{node}(9350)
                        └─{node}(9351)
```

View the system top using `systemd-cgtop` like so:

```
systemd-cgtop
```

View the system processes as a recursive list using `systemd-cgls` like so:

```
systemd-cgls
```

## Disk usage and folders

Find the size of **all folders** under the `/mnt` directory:

```
du -h /mnt
```

If you want to show only the size of the reqested folder using the `-s` switch:

```
du -sh /mnt
```

View disk usage for the top level folders only:

```
du -h -d1 /
```

Sort the output from `du`:

```
du -hs * | sort -h
```

## Mounting and Unmounting Disks

Checking disk mounts, file systems and so on:

```
lsblk -f
file -s /dev/sdf
fsck -N /dev/sdf
```

Mounting a drive is pretty simple:

```
mount /dev/sdf /mnt
```

Specify the file system to use:

```
mount -t ext4 /dev/sdf /mnt
```

Unmounting a drive is also pretty simple:

```
umount /mnt
```

## fstab

Its always a good idea to use `fstab` for mounting drives automatically. Usually a good place to check if drives are not mounting / unmounting as expected:

```
nano /etc/fstab
```

## Extend a Linux file system after resizing a volume

Taken from the AWS Article [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html).

Basiclly, after resizing an EBS volume via the AWS EC2 Console you need to extend the file system in the Linux terminal of the server like so:

1. Check your file system parameters

```
df -hT
lsblk
```

2. Run `growpart` command on the extended partition

```
sudo growpart /dev/nvme1n1 1
```

3. Run `resize2fs` (for `ext4` filesystms) on the mounted drive:

```
sudo resize2fs /dev/nvme1n1p1
```

4. Check using `df -h` to view the newly resized drive!

```
df -h
```

## Grep

Search for something except in one folder (e.g. node_modules)

```
grep -R --exclude-dir=node_modules 'some pattern' /path/to/search
```

Exlude multiple directories using a Glob:

```
grep -r oscar --exclude-dir={node_modules,.webpack} .
```

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

...or using Python

```
python3 -m http.server
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

### Disk I/O speedtest

**Disk Write**

dd if=/dev/zero of=/mnt/speedtest/deleteme.dat bs=32M count=64 oflag=direct

**Disk Read**

dd if=/mnt/speedtest/deleteme.dat of=/dev/null bs=32M count=64 iflag=direct

### View full system architecture

Nice shortcut command to view linux system architecture:

```
lscpu
```

### Create a file fingerprint (MD5)

```
mdf file
```

### Create a file fingerprint (sha1sum)

```
sha1sum file
```

### Speedtest using just python

```
curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3 -
```

### Check if the disk is a HDD or a SSD

If the following command returns a 1 then it is a spinning disk (HDD) and if it returns 0 its an SSD.

```
cat /sys/block/sda/queue/rotational
```

Note sometimes you might need to replace `sda` with `sdb`.

You can alternaively use this command:

```
lsblk -d -o name,rota
```

### Create new user on Ubuntu

```
#!/bin/bash
set -euo pipefail

USERNAME=developer

# Create user and immediately expire password to force a change on login
useradd --create-home --shell "/bin/bash" --groups sudo "${USERNAME}"
passwd --delete "${USERNAME}"
chage --lastday 0 "${USERNAME}"

# Create SSH directory for sudo user and move keys over
home_directory="$(eval echo ~${USERNAME})"
mkdir --parents "${home_directory}/.ssh"
cp /root/.ssh/authorized_keys "${home_directory}/.ssh"
chmod 0700 "${home_directory}/.ssh"
chmod 0600 "${home_directory}/.ssh/authorized_keys"
chown --recursive "${USERNAME}":"${USERNAME}" "${home_directory}/.ssh"

# Disable root SSH login with password
sed --in-place 's/^PermitRootLogin.*/PermitRootLogin prohibit-password/g' /etc/ssh/sshd_config
if sshd -t -q; then systemctl restart sshd fi
```

### Hostname

Change the hostname on Ububtu:

```
hostnamectl set-hostname viveks-laptop
```

### Change password of current user

Simply run `passwd` and follow the instructions.

### Using rsync to copy data from machine to machine

Lets say you have two EC2 instances and one has some data on epemeral storage that you want to copy over to another instance that has EBS storage. Then the `rsync` command can come to your rescue!

The below command will sync/copy all data from the source computer @hostname folder `/source/folder/` to the destination computer (which is where you run this command - on the destination computer) folder `/destination/folder/`.

NOTE: `rsync` uses SSH protocol so you need to

1. Add the public key of the destination computer TO the _source computers_ `~/.ssh/authorized_keys` file
1. Whitelist the Private IP address of the destination computer in the *Inbound Security Group Settings* for the _source computer_.

```
rsync -avzlh --stats username@hostname:/source/folder/  /destination/folder/ > /var/log/rsync-status.log
```

### Listening Network Interfaces

Using `netstat`:

```
netstat -lnt
```

### Check services are enabled to restart or not (under STATE col).
sudo systemctl list-unit-files --type=service

### Enable services to start up on reboot
sudo systemctl enable your-fine-service

### Disable services starting up on reboot
sudo systemctl disable your-fine-service
update-rc.d -f proftpd remove

### Journalctl

### Filter logs

Show all logs of bot:

```
journalctl -u bot
```

Since a specific date:

```
journalctl --since "2020-11-16 11:10" -u bot
```

Last n lines since a sepecific amount of time:

```
journalctl -u bot -n 50 --since "1 hour ago"
```

Logs containing specific string

```
journalctl -u bot | grep a09b0280
```

or

```
journalctl -u bot -n 50 --since "1 minute ago" | grep something
```

### Purge logs

Check the disk usage of journals:

```
journalctl --disk-usage
```

You can set this in `/etc/systemd/journald.conf` to keep the log file below a specified size like so:

```
SystemMaxUse=100M
```

Check disk usage:

```
journalctl --disk-usage
```

If the logs get too large then they can be manually purged using these couple of examples (check `man journalctl` for more information.)

**Clear all logs**

Run both of the below commands one after the other.

```
sudo journalctl --rotate
sudo journalctl --vacuum-time=1s
```

**Clear a subset of logs**

To clear just a subset of logs, use the following examples:

```
// Retain the last 2 days
journalctl --vacuum-time=2d
```

or

```
// Retain 100 MB of logs
journalctl --vacuum-size=100M
```