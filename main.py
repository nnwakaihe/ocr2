import pytesseract
from PIL import Image
from tkinter import Tk, Text, Scrollbar, Frame, Button, messagebox
from tkinter.filedialog import askopenfilename

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
    button = Button(root, text="Close", command=root.destroy)
    button.pack()

    # Run the Tkinter event loop
    root.mainloop()

def main(image_path=None):

    # Prompt the user to select a file using the file explorer
    root = Tk()
    root.withdraw()

    if image_path is None:
        image_path = askopenfilename()

    if image_path:
        try:
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            text = pytesseract.image_to_string(Image.open(image_path))
            show_extracted_text(text)  # Display extracted text in a pop-up window
            root.destroy()  # Close the pop-up window
        except ValueError:
            messagebox.showinfo("Error", "Failed to extract text from the image.")
    elif image_path == "":
        messagebox.showinfo("Error", "No file selected.")

if __name__ == '__main__':
    main()
