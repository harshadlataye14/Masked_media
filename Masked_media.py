import os
from media_lib import image_stego, audio_stego, text_stego

def steganography_tool():
    print("""
    __  ___           __            __     __  ___         ___      
   /  |/  /___ ______/ /_____  ____/ /    /  |/  /__  ____/ (_)___ _
  / /|_/ / __ `/ ___/ //_/ _ \/ __  /    / /|_/ / _ \/ __  / / __ `/
 / /  / / /_/ (__  ) ,< /  __/ /_/ /    / /  / /  __/ /_/ / / /_/ / 
/_/  /_/\__,_/____/_/|_|\___/\__,_/____/_/  /_/\___/\__,_/_/\__,_/  
                                 /_____/                            

Supports PNG, TXT, and WAV file formats for embedding and extracting hidden data.

""")
    print("Welcome to Steganography Tool!")
    print("Choose an option:")
    print("1. Encode message")
    print("2. Decode message")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice! Please enter either 1 or 2.")
        return

    n = 0 if choice == '1' else 1

    file_type = input("Enter the type of file (image, audio, txt): ")

    if file_type not in ['image', 'audio', 'txt']:
        print("Invalid file type! Please enter one of: image, audio, txt.")
        return

    file = input("Enter the path to the {} file: ".format(file_type))

    if not os.path.isfile(file):
        print("File not found! Please enter a valid file path.")
        return

    file_extension = os.path.splitext(file)[1].lower()

    if file_type == 'image' and file_extension not in ['.png']:
        print("Invalid file extension for image! Please use .png")
        return

    elif file_type == 'audio' and file_extension != '.wav':
        print("Invalid file extension for audio! Please use .wav.")
        return

    elif file_type == 'txt' and file_extension != '.txt':
        print("Invalid file extension for text! Please use .txt.")
        return

    if file_type == 'image':
        if n == 0:
            image_stego.image_steg(file, n)
            print("Message encoded successfully!")
        else:
            image_stego.image_steg(file, n)
            print("Decoding completed successfully!")

    elif file_type == 'audio':
        if n == 0:
            audio_stego.Audio_steg(file, n)
            print("Message encoded successfully!")
        else:
            audio_stego.Audio_steg(file, n)
            print("Decoding completed successfully!")
    
    elif file_type == 'txt':
        if n == 0:
            text_stego.Text_steg(file, n)
            print("Message encoded successfully!")
        else:
            text_stego.Text_steg(file, n)
            print("Decoding completed successfully!")

if __name__ == "__main__":
    steganography_tool()

