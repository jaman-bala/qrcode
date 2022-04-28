import qrcode

img = qrcode.make("https://www.mvd.gov.kg")
img.save('myQr.jpg')
