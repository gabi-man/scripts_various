#Imports
import os
import time
from pathlib import Path
import shutil
import subprocess


#Constants
BASE_PATH = Path(__file__).parent.resolve()
#BASE_PATH = Path('/home/gabriel/Documents/test/')
input_dir = BASE_PATH / 'inputs'
process_dir = BASE_PATH / 'process' 
vertical_dir = BASE_PATH / 'Videos-V'
horizontal_dir = BASE_PATH / 'Videos-H'
date_and_time = time.strftime("%d-%m-%y_%H-%M-%S")

    


#Functions Definitions
def search_jpg():
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('hor.jpg'):
            resolution = 'hor'
        elif filename.lower().endswith('ver.jpg'):
            resolution = 'ver'
        else:
            print(f"Files with another extension, please remove then and try again --> {date_and_time}", 
            file= open (BASE_PATH/'log.txt', "a"))
            raise ValueError("This is shit")

        move_jpg(filename)
        saved_mp4 = converter_to_mp4(filename, resolution)
        move_mp4(saved_mp4, resolution)
        if not saved_mp4:
            print(f"Dont Convert these videos --> {date_and_time}", 
            file= open (BASE_PATH/'log.txt', "a"))
            raise Exception("Dont Convert these videos")
        else:
            print(f"Video {saved_mp4} convert successfully --> {date_and_time}", 
            file= open (BASE_PATH/'log.txt', "a"))
            print("*" *30 , file= open (BASE_PATH/'log.txt', "a"))
        

def move_jpg(file):
    if os.path.isfile(os.path.join(input_dir, file)):
        os.remove(os.path.join(input_dir, file))
        print(f"Duplicate file {file} was found and deleted  --> {date_and_time}", 
            file= open (BASE_PATH/'log.txt', "a")) 
    else:
        shutil.move(os.path.join(input_dir, file), process_dir)
    

def converter_to_mp4(file, resolution):
    if resolution == 'hor':
        res = '1920x1080'
    elif resolution == 'ver':
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
    if resolution == 'hor':
        directory = vertical_dir
    elif resolution == 'ver':
        directory = horizontal_dir
    else:
        print(f"Dont move these videos --> {date_and_time}", 
            file= open (BASE_PATH/'log.txt', "a"))
        raise Exception("Dont move these videos")

    if os.path.isfile(os.path.join(directory, file)):
        os.remove(os.path.join(directory, file))
        print(f"Duplicate video {file} was found and deleted --> {date_and_time}", 
            file= open (BASE_PATH/'log.txt', "a")) 
    else:
        shutil.move(os.path.join(process_dir, file), directory)
    


    

 

if __name__ == '__main__':
    search_jpg()