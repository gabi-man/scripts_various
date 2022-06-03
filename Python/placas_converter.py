#Imports
import os
import time
from pathlib import Path
import shutil
import subprocess


#Constants
BASE_PATH = Path('/home/gabriel/Documents/test/')
input_dir = BASE_PATH / 'inputs'
process_dir = BASE_PATH / 'process' 
vertical_dir = BASE_PATH / 'Videos-V'
horizontal_dir = BASE_PATH / 'Videos-H'
date_and_time = time.strftime("%d-%m-%y_%H-%M-%S")
    


#Functions Definitions
def search_jpg():
    for filename in os.listdir(input_dir):
        if filename.endswith("HOR.jpg"):
            move_jpg(filename)
            saved_mp4 = converter_to_mp4(filename, resolution="HOR")
            move_mp4(saved_mp4, 'HOR')
        elif filename.endswith("VER.jpg"):
            move_jpg(filename)
            saved_mp4 = converter_to_mp4(filename, resolution="VER")
            move_mp4(saved_mp4, 'VER')
        else:
            print(f"No se movio los archivos --> {date_and_time}", file= open (process_dir/archivo_log, "a"))
        

def move_jpg(file):
    shutil.move(os.path.join(input_dir, file), process_dir)
    

def converter_to_mp4(file, resolution):
    if resolution == 'HOR':
        res = '1920x1080'
    elif resolution == 'VER':
        res = '720x1280'
    else:
        print("No encontre nada")

    command = ' '.join([
        'ffmpeg',
        '-loop 1',
        f'-i {process_dir/file}',
         f'-s {res}',
        '-t 30',
        '-vcodec libx264',
        '-profile:v main ',
        '-pix_fmt yuv420p',
        '-vf "fade=t=in:st=0:d=1,fade=t=out:st=29:d=1"', 
        f'{process_dir/file[:-4]}.mp4'
    ])
    subprocess.run([command], shell=True)
    return f'{process_dir/file[:-4]}.mp4'


def move_mp4(file, resolution):
    if resolution == 'HOR':
        shutil.move(os.path.join(process_dir, file), horizontal_dir)
    else:
        shutil.move(os.path.join(process_dir, file), vertical_dir)

    

 

if __name__ == '__main__':
    #converter_to_mp4("Show_03_06_HOR.jpg")
    search_jpg()