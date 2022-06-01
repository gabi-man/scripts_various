#Imports
import os
import time
from pathlib import Path
import shutil

#Variables
input_dir = Path("/home/gabriel/Documents/test/inputs")
process_dir = Path("/home/gabriel/Documents/test/process")
date_and_time = time.strftime("%d-%m-%y_%H-%M-%S")





        



def search_jpg():
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg"):
            move_jpg(filename)
        else:
            print(f"No se movio los archivos --> {date_and_time}", file= open (process_dir/archivo_log, "a"))
        

def move_jpg(file):
    shutil.move(os.path.join(input_dir, file), process_dir)

def converter():
    pass

def move_mp4():
    pass

search_jpg()