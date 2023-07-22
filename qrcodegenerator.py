import qrcode

qr = qrcode.QRCode(
    version=15, #15 means the version of the qr code, higher the number, bigger the qr code image and complicated is the picture
    #The range of version is from 1 to 40
    box_size=10, # size of the box where qr code will be displayed
    border=5 #it is the white part of image -- border in all 4 sides with white color
)

data=input("Enter the data(Name/Number or Url): ") #The input should not conatain space

qr.add_data((data))
qr.make(fit=True)
img = qr.make_image(fill="black", back_color = "white")
img.save("output.png")