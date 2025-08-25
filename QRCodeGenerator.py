import qrcode

while True:
    try:
        unique_qr = int(input("how many URLs do you want to enter? "))
        if unique_qr >= 1:
            break
    except ValueError:
        print("Enter valid integer")
        continue

mylist = []

while unique_qr > 0:
    website = input("Enter URLs to get QR Codes ")
    color_fill = input("Enter fill color: ")
    color_back = input("Enter back color: ")

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(website)
    qr.make(fit=True)
    try:
        img = qr.make_image(fill_color=color_fill, back_color=color_back)
    except ValueError:
        print("Enter a valid color name!")
        continue

    file_name = input("Enter the file name: ")
    mylist.append(file_name)
    img.save(f"{file_name}")
    unique_qr -= 1

print("All files are: ", mylist)

