# install all the liblaries needed
# pip install -r requirements.txt
# create the function that collect a text and convert it to a qrcode
# save qr code as an image
# run the function

import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    name_img = input("Save nama file: ")
    image_path = "p7_qr_code_generator/qrcode"
    img.save(f"{image_path}/{name_img}.png")


codeUser = input("Input link: ")
generate_qrcode(codeUser)
