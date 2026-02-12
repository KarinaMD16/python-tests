import qrcode

# This file contains a simple QR code generator that prompts 
# the user for input and saves the generated QR code as a PNG file.

choice = input("How many QR codes do you want to generate?: ")

for i in range(int(choice)):
    data = input('Enter the text or URL: ').strip()
    filename = input('Enter the filename: ').strip()
    color = input('Enter the color (black/white): ').strip().lower()

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    image = qr.make_image(fill_color=color, back_color='white')
    image.save(filename + ".png")
    print(f'QR code saved as {filename}')