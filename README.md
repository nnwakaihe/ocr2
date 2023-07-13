# OCR
 Takes image input and returns a text from said image.

 Before running:
 - Install "tesseract-ocr-w64-setup-5.3.1.20230401.exe" file found in repo, or download the latest version here https://github.com/UB-Mannheim/tesseract/wiki 
 - Save the path for the installed tesseract.exe file as an environment variable called "tessreact_path".


The code can be run as an executable application. 
- Install "pyinstaller".
- Run the following terminal command in the project directory: pyinstaller --name ocr_app --onefile main.py
- A ocr_app.exe file will be available in the \dist folder of the project.
- You can double-click the application, or drag and drop an image file on the application to run the program.

 
