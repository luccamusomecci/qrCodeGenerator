import qrcode 

print('Put the link: ')
link = input()

imge = qrcode.make(link)

print('Name of the file (leave it blank and it will be code.jpg): ')
name = input()

if len(name) is 0:
    name = "code"

imge.save(name + ".jpg")

