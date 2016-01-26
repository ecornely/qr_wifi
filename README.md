# QR-code Wifi
This project contains a simple python cgi script that generate QR-code with wifi information

## OVH installation

I used it on an OVH shared server able to do CGI but it requires you to install a few python modules which is not allowed on shared servers
What I did is download qrcode-5.1.tar.gz, setuptools-19.6.tar.gz, six-1.10.0.tar.gz, pymaging-master.zip, pymaging-png-master.zip and from the remote shell used their setup.py with a prefix.

setup.py install --prefix=/homez.62/ecornely/python_lib

That's why in the code I have to append things to the sys.path
