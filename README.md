# OCR_project
The overall plan for this project is to OCR pdfs via the web.

I plan for the actual code doing the OCR to be in Python, using Tesseract. The web portion will be a JS framework, likely React.  

In addition, there would be the basic functionality of rotating, extracting pages from, and combining multiple individiual pdfs into a single pdf.  

**Stretch goals:** I want to have a system that can be accessed anywhere via the web, and *ideally* would OCR pages faster than using Adobe Pro.  I'm guessing the latter would be pretty hard, though. :)

Maybe, just maybe, I can get this project ported to work in WebAssembly.  Dunno if that would actually help with speed.

## Tutorial
The commmand to run ocr.py on a plain image with text:
 * `python ocr.py --image [your image directory]/your_example_image.png`

 Now, try testing the program with a noisy image (tough to do!):
 * `python ocr.py --image images/example_02.png --preprocess blur`

 