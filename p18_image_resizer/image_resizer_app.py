# install pillow
# import pillow
# open up the image we want to resize using python
# print the current size of that image
# specify the size we wanna change it to
# save the new resize

from PIL import Image  # PIL is pillow


def resize_image(size1, size2):
    # change the image
    resized_img = img.resize((size1, size2))

    # save the image
    print("")
    new_name = input("Enter the new name: ")
    resized_img.save(f'p18_image_resizer/new_img/{new_name}.jpeg')
    img_new = Image.open(f'p18_image_resizer/new_img/{new_name}.jpeg')
    print("")
    print("Here the result")
    print(f"New size: {img_new.size}")


print("Make sure the image must be in this folder !")
input_img = input("Input the file name: ")
img = Image.open(f'p18_image_resizer/{input_img}.jpeg')
print(f"Current size: {img.size}")
print("")
print("Then enter the size")
size1 = int(input("Enter width: "))
size2 = int(input("Enter length: "))
resize_image(size1, size2)
