import cv2
from pytesseract import pytesseract
from gtts import gTTS
import os
# Update with your Tesseract path
pytesseract.tesseract_cmd = r'C:\Users\91832\AppData\Local\Programs\Tesseract-OCR'
# Load the image
img = cv2.imread(r"C:\Users\91832\Pictures\Jovian.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extract text from image
import subprocess

# Save the grayscale image to a temporary file
cv2.imwrite('temp_image.png', gray)

# Run Tesseract using subprocess
command = [r'C:\Users\91832\AppData\Local\Programs\Tesseract-OCR\tesseract.exe', 'temp_image.png', 'output', '--psm', '6']
proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Read the output text
with open('output.txt', 'r') as file:
    extracted_text = file.read()

print("Extracted Text: ", extracted_text)
print("Extracted Text: ", extracted_text)
# Convert text to speech
tts = gTTS(text=extracted_text, lang='en')

# Save the speech to a file
tts.save('output_audio.mp3')

# Play the audio file
os.system('start output_audio.mp3')
