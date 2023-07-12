import logging
import pytesseract
from PIL import Image


def main():
    logging.info('Python script started.')

    # Get the image file
    image_file = 'my_image.jpg'

    # Convert the image to text
    text = pytesseract.image_to_string(Image.open(image_file))

    # Print the text
    print('Text extracted from image: {}'.format(text))


if __name__ == '__main__':
    main()
