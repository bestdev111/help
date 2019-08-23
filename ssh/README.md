## SSH 

`ssh-keygen` *Generates a new public keypair*

`pbcopy < ~/.ssh/id_rsa.pub` *Securly copy your SSH key to your clipboard*

`ssh-keygen -p -f some-keypair.pem` *Encrypt a private key file*

`ssh-add -K ~/.ssh/id_rsa_somenewkey` *Add the new key to the ssh agent so its used when attempting to authenticate*