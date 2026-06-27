import qrcode

# Right now it points to your local testing page. 
# You can change this to your live website domain later!
website_url = "http://localhost:5000" 

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(website_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("dj_cali_love_qr.png")

print("QR Code generated successfully as 'dj_cali_love_qr.png'!")

