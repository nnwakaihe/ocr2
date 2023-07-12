import logging
import pytesseract
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def main():
    logging.info('Running the script locally.')

    # Prompt the user to select a file using the file explorer
    root = Tk()
    root.withdraw()
    image_path = askopenfilename()

    if image_path:
        try:
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            text = pytesseract.image_to_string(Image.open(image_path))
        except ValueError:
            text = ''
        print('Text Extracted from Image:', text)
    else:
        print('No file selected.')


if __name__ == '__main__':
    main()
