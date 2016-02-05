# image to base64 for encryption



import base64

with open("images/worst_tech_nova_nuwave_12.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    print(encoded_string)


# with open("images/worst_tech_nova_nuwave_12.png", "rb") as f:
#    data = f.read()
#    print(data.encode("base64"))
