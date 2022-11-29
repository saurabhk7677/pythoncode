# import qrcode

# qr=qrcode.QRCode(
#     version=15,
#     box_size=10,
#     border=5
# )

# data = 'https://www.youtube.com/watch?v=It57Mjm09pk'
# qr.add_data(data)
# qr.make(fit=True)
# img = qr.make_image(fill="black", back_color="white")
# img.save('text.png')


import random

otp = random.randrange(10000,1000000)
print(otp)

user = int(input("Enter the OTP: "))
if otp == user:
    print("Access Granted...!!!!")

else:
    print("Access Denied...!!!!!")