import qrcode

# Text to be converted to QR code
text = "Your Text Goes Here!"

# Create QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add data
qr.add_data(text)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qr_code.png")
