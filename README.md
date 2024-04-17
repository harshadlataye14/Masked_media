# Masked_media
# Overview

Masked_media is a Python tool designed for hiding and extracting secret messages in media files such as images, audio, and text files. This tool uses steganography techniques to embed and retrieve messages, making it a useful tool for secure communication.

![Screenshot 2024-04-15 105325](https://github.com/harshadlataye14/Masked_media/assets/57581998/e381a20c-7795-4c42-8a00-a948c0918df3)


# Requirements

Install Python: If you haven't installed Python yet, download and install it from python.org.

**Install Required Python Modules:**


cv2: For image processing and manipulation.

    pip install opencv-python

wave: (No separate installation needed as it's part of Python's standard library)

PIL (Pillow): For handling image files and their pixel data.

    pip install Pillow

numpy: For numerical operations and array manipulations.

    pip install numpy

**Or Yoc Can Do**
    
    pip install -r requirments.txt

# Usage
**Clone the Repository:**

    git clone (https://github.com/harshadlataye14/Masked_media.git)

**Navigate to the Directory:**

    cd masked_media

**Run the Script:**

    python masked_media.py

**Select Mode:**

Choose between encode or decode mode.

**Select File Type:**

Choose the file type you want to work with: png, txt, or audio.

**Enter File Path:**

Provide the path to the file you want to encode or decode.

**Enter Secret Message:**

If you are in encode mode, enter the secret message you want to hide.

If you are in decode mode, the tool will display the hidden message from the file.


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


