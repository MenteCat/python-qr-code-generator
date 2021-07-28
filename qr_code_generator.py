import qrcode
 
#Link to the CV 
input_data = "https://drive.google.com/file/d/1zkuv1_Tpuc1z1CGaGg8f6VS6hCrAO-ER/view?usp=sharing"

#Instance of qrcode
qr = qrcode.QRCode(
    version=2,
    box_size=10,
    border=5,
)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill_color='midnightblue', back_color='white')
img.save('qrcodeCV.png')
