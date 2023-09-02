# GIF Splitting Engine built by @heyjude007 on GitHub
print("Coded by Seb Johnstone, with help from Judith Greaney")
print("Starting Judith's Splitter for gifs....")

# Splif GIF Splitter
# Coded by Judith Greaney 2023
# Version 0.1.0
# import Pillow library
import PIL
from PIL import Image
# Imports GIF file and extracts frames, saves to destination


def frameExtract(gifpath, dest):
    global frame
    img = Image.open(gifpath)
    try:
        frame = 0
        while True:
            currentframe = img.copy()
            currentframe = currentframe.convert('RGB') # Converts the frame to RGB, otherwise the code exits with an error
            currentframe.save(f"{dest}/frame{img.tell()}.jpg")
            frame += 1
            img.seek(frame)
    except EOFError:
        pass
    finally:
        img.close()

print("Splif GIF Splitter v0.1.0")
print("Coded by Judith Greaney 2023")
gifpath = input("Enter the path to your gif here:").strip('\'"')
dest = "imgoutput"
frameExtract(gifpath, dest)

dest = "imgoutput/"

frame -= 1
name_list = []
for num in range(0, frame):
    name_list.append(num)

time = 0
first_time = True

def filenamefinder():
    global path, time, first_time
    if first_time == True:
        path = f'{dest}frame0.jpg'
        time += 1
        first_time = False
    else:
        time += 1
        path = f'{dest}frame{time}.jpg'
        

# Use Modified Image to Ascii TXT files.
path = dest
number = frame
name = f'{"text_output/" + "ascii_img" + str(number) + ".txt"}'

for images in range(0, number):
    if images > number:
        break
    img_flag = True
    filenamefinder()
    name = f'{"textoutput/" + "ascii_img" + str(images) + ".txt"}'
    try:
        img = PIL.Image.open(path)
        img_flag = True
    except:
        print(path, "Unable to find image ");
    images = 1
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    
    img = img.convert('L')
    
    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
    
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    
    with open(name, "w") as f:
        f.write(ascii_image)