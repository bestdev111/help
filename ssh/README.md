## SSH

`ssh-keygen` *Generates a new public keypair*

`pbcopy < ~/.ssh/id_rsa.pub` *Securly copy your SSH key to your clipboard*

`ssh-keygen -p -f some-keypair.pem` *Encrypt a private key file*

`ssh-add -K ~/.ssh/id_rsa_somenewkey` *Add the new key to the ssh agent so its used when attempting to authenticate*

### SSH Config

To add alias ssh hosts, use a config file. First, create the file if it does not already exist: `touch ~/.ssh/config && chmod 600 ~/.ssh/config`

Then add contents to it like the following example:

```
Host somehost
    HostName 19.01.22.13
    User myusername
    Port 22
    IdentityFile ~/.ssh/id_rsa

Host someotherhost
    HostName 178.222.99.90
    User auser
    Port 2022
    IdentityFile ~/.ssh/id_rsa
```

So naturually, its possible to easily use a different public keys depending on the server. For more details check out [this article](https://linuxize.com/post/using-the-ssh-config-file/).

### SHA

To hash a phrase, use the following:

```
echo -n 'I call heads. And I have a secret. I hate your lasagna.' | shasum -a 256
```

### SCP - Secure Copy Files

To copy a file from a local machine to a remote machine using SSH:

```
scp <source> <destination>
scp /path/to/file username@a:/path/to/destination
```