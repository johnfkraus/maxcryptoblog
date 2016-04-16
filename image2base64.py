import base64
import sys
import inspect

def lineno():
    # Returns the current line number in our program.
    return str(inspect.currentframe().f_back.f_lineno) + ' '

# convert an image to base64 text

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


def image2text(imageFilePath, textFilePath):
	with open(imageFilePath, 'rb') as image_file:
		encoded_string = base64.b64encode(image_file.read())
		# print(encoded_string)
	f = open(textFilePath, 'w')
	f.write(str(encoded_string))
	f.close()
	return True


# encrypt the text...


# decrypt the text...


# convert the text back to an image
def text2image(textFilePath, imageFilePath):
	#ft = open(textFilePath, 'r')
	#image_data = ft.read()
	print(lineno() + 'textFilePath = ' + textFilePath)
	print(lineno() + 'imageFilePath = ' + imageFilePath)
	fh = open(imageFilePath, "wb")
	with open(textFilePath, 'r') as text_file:
		read_text_file = text_file.read() #.decode('base64')	
		print(lineno() + read_text_file[0:300] + ' ... ' )
		print(lineno() + str(type(read_text_file)))
		b = bytes(read_text_file, 'utf-8')
		print(lineno() + str(type(b)))
		fh.write(b)
		# fh.write(text_file.read().decode('base64'))
		fh.close()
	#ft.close()
	return True


def test():
	encoded_file_extension = '.encoded.txt'
	decoded_file_extension = '.decoded.jpg'
	image_file = 'weed4.jpg'
	encoded_filename = image_file + encoded_file_extension
	decoded_filename = encoded_filename + decoded_file_extension
	image2text(image_file, encoded_filename)
	text2image(encoded_filename, decoded_filename)
	print('done')


#	encoded_string = base64.b64encode(image_file.read())
#	print(encoded_string)
#fh.write(imgData.decode('base64'))
#fh.close()



def main():
	args = sys.argv[1:]

	if not args:
	    print('usage: [--test]')
	    sys.exit(1)

	if args[0] == '--test':
		test()


if __name__ == '__main__':
    main()
