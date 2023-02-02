import qrcode
from PIL import Image
# CODE QR
qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,border=3)
qr.add_data("https://www.w3school.org/")
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white")
img.save("my_code.png")
