import pytesseract
from PIL import Image
from tkinter import Tk, Text, Scrollbar, Frame, Button, messagebox
from tkinter.filedialog import askopenfilename
import argparse
import sys
import os

def show_extracted_text(text):
    root = Tk()
    root.title("Text Extracted from Image")

    # Create a Frame to hold the Text widget and Scrollbar
    frame = Frame(root)
    frame.pack(fill='both', expand=True)

    # Create a Text widget and Scrollbar
    text_widget = Text(frame, wrap='word')
    scrollbar = Scrollbar(frame, command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)

    # Pack the Text widget and Scrollbar
    text_widget.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    # Insert the extracted text into the Text widget
    text_widget.insert('1.0', text)

    # Disable editing of the Text widget
    text_widget.config(state='disabled')

    # Create a Close button to close the window
    button = Button(root, text="Close", command=lambda: [root.destroy(), sys.exit()])
    button.pack()

    # Run the Tkinter event loop
    root.mainloop()

def main(image_path=None):
    if image_path is not None:
        try:
            tesseract_path = os.environ.get('TESSERACT_PATH')
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
            text = pytesseract.image_to_string(Image.open(image_path))
            show_extracted_text(text)  # Display extracted text in a pop-up window
        except ValueError:
            messagebox.showinfo("Error", "Failed to extract text from the image.")
    else:
        messagebox.showinfo("Error", "No file selected.")

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', nargs='?', default=None, help='Path to the image file')
    args = parser.parse_args()

    # If an image file is provided as a command-line argument, use it as the image_path
    if args.image_path is not None:
        main(args.image_path)
    else:
        # Prompt the user to select a file using the file explorer
        root = Tk()
        root.withdraw()
        image_path = askopenfilename()

        main(image_path)

# To build the .exe application running the following commands in the terminal. The .exe file can then be found in the \dist folder:
# pyinstaller --name ocr_app --onefile main.py
# pyinstaller ocr_app.spec