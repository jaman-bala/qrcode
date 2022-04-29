import qrcode

img = qrcode.make("https://www.instagram.com/black_list.kg/")
img.save('myQr-insta.jpg')
