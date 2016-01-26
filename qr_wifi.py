#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Add libraries installed in a specific folder to the python path
import sys
sys.path.insert(0, "/homez.62/ecornely/python_lib/lib/python2.6/site-packages")
sys.path.insert(0, "/homez.62/ecornely/python_lib/lib/python2.6/site-packages/qrcode-5.1-py2.6.egg")
sys.path.insert(0, "/homez.62/ecornely/python_lib/lib/python2.6/site-packages/six-1.10.0-py2.6.egg")
sys.path.insert(0, "/homez.62/ecornely/python_lib/lib/python2.6/site-packages/setuptools-19.6-py2.6.egg")
sys.path.insert(0, "/homez.62/ecornely/python_lib/lib/python2.6/site-packages/pymaging-0.1-py2.6.egg")
sys.path.insert(0, "/homez.62/ecornely/python_lib/lib/python2.6/site-packages/pymaging_png-0.1-py2.6.egg")

#Import libraries
import cgi
import qrcode
import PIL
from PIL import Image

def generate(info="WIFI:S:mynetwork;T:WPA;P:mypassword;;"):
    """Generates a QR-code from a string and returns a PIL Image object"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=0,
        )
    qr.add_data(info)
    qr.make(fit=True)

    img = qr.make_image()
    #If image is not 555 px resize it
    if( img.size[0] != 555 ):
        img = img.resize( (555,555), PIL.Image.ANTIALIAS)
    # Convert from b/w to RGB
    img = img.convert(mode="RGB")
    #Load logo
    logo=Image.open("logo.png")
    #Insert the wifi logo at 185/185 px
    img.paste(logo, (185,185))
    return img

# CGI part to get form information
params = cgi.FieldStorage()
ssid = params.getvalue("SSID")
password = params.getvalue("PASSWORD")
if ssid == None or len(ssid)==0 or password == None or len(password)==0 :
    print("Content-type: text/html\n\n")
    print("""<!DOCTYPE html>
<html>
    <head>
        <title>Wifi QRCode generator</title>
    </head>
    <body>
        <h1>Wifi QRCode generator</h1>
        <p>This python CGI is able to generate a QRCode that smartphones should be able to read and use to automatically connect to a wifi network protected by a WPA password</p>
        <form action="qr_wifi.py" method="get">
            <div>
                <label>Network SSID : <input type="text" name="SSID"/></label>
            </div>
            <div>
                <label>Password : <input type="text" name="PASSWORD"/></label>
            </div>
            <div>
                <input type="submit" value="Generate"/>
            </div>
        </form>
    </boddy>
</html>\n\n""")
else:
    qr = generate("WIFI:S:%s;T:WPA;P:%s;;" % (ssid, password))
    sys.stdout.write("Pragma-directive: no-cache\n")
    sys.stdout.write("Cache-directive: no-cache\n")
    sys.stdout.write("Pragma: no-cache\n")
    sys.stdout.write("Expires: 0\n")
    sys.stdout.write("Cache-Control: no-store, no-cache, must-revalidate\n")
    sys.stdout.write("Content-type: image/png\n\n")
    qr.save(sys.stdout, "PNG")
