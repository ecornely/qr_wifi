import qrcode
import PIL
from PIL import Image
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=0,
)
qr.add_data("WIFI:S:toto;T:WPA;P:prout;;")
qr.make(fit=True)

img = qr.make_image()
if(img.size[0] != 555):
    img = img.resize( (555,555), PIL.Image.ANTIALIAS)
img = img.convert(mode="RGB")

logo=Image.open("logo.png")

img.paste(logo, (185,185))
img.save("qrcode.png")
