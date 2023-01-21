from PIL import Image
import pillow_heif
import glob, os
from tqdm import tqdm
import os
from sys import exit
import time

if not glob.glob("*.heic"):
    print("No HEIC file found in the current folder. Please move the executable to a folder containing HEIC images.")
    time.sleep(5)
    exit()

for file in tqdm(glob.glob("*.heic")):
    print("Converting: " + file + "....", end='\r')
    heif_file = pillow_heif.read_heif(file)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )

    isExist = os.path.exists('./JPG')
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs('./JPG')
    image.save("./JPG/" + file + ".jpeg", format("JPEG"))


print("Thanks for using Achyuth's HEIC to JPEG conversion program :)")
