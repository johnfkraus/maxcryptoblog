import base64


# convert an image to base64 text

def image2text(imageFilePath, textFilePath):
	with open('justice.jpg', 'rb') as image_file:
		encoded_string = base64.b64encode(image_file.read())
		# print(encoded_string)

	f = open("justice.txt", 'w')
	f.write(encoded_string)
	f.close()
	return True

# encrypt the text...



# decrypt the text...



# convert the text back to an image

def text2image(textFilePath, imageFilePath):

	#ft = open(textFilePath, 'r')
	#image_data = ft.read()

	fh = open(imageFilePath, "wb")

	with open('justice.txt', 'r') as text_file:
		fh.write(text_file.read().decode('base64'))
		fh.close()
	#ft.close()
	return True

textFilePath = 'justice.txt'
image2text('justice.jpg', textFilePath)

text2image(textFilePath, 'justice2.jpg')


#	encoded_string = base64.b64encode(image_file.read())
#	print(encoded_string)
#fh.write(imgData.decode('base64'))
#fh.close()


