# Install tesseract to your machine
# If on a mac use homebrew
from PIL import Image
import pytesseract
import numpy as np

# Enter the file name that you need over here
filename = 'fileName'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)