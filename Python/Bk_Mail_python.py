# Modules
import os
import time
from pathlib import Path
import tarfile
import shutil

# Constants
BASE_PATH = Path(__file__).parent.resolve()
date_and_time = time.strftime("%d-%m-%y_%H:%M:%S")
date = time.strftime("%d-%m-%y")
file_name = f"Thunder_{date}.tgz"
destination_dir = BASE_PATH / "Bk_email_automatico"
source_dir = Path("/home/gabriel/.thunderbird")
log_file = destination_dir / "log_bk.txt"
compress_file = source_dir / file_name
days = 14
now = time.time()

# Functions definitions

# We create a directory if it isn't exists
# Add log output to watch result of script


def make_dir():
    try:
        os.mkdir(destination_dir)
    except OSError:
        print(
            f"Failed to create a directory, because directory exists  --> {date_and_time}", file=open(log_file, "a"))
    else:
        print(
            f"Directory was created successfuly: %s --> {date_and_time}", file=open(log_file, "a"))

# Check if file exists


def make_compress():
    if os.path.exists(destination_dir / file_name):
        print(
            f"Dont create the file because it already exists--> {date_and_time}", file=open(log_file, "a"))
    else:
        with tarfile.open(compress_file, "w:gz") as tar:
            os.chdir(source_dir)
            for name in os.listdir("."):
                tar.add(name)
                print(name)
            shutil.move(os.path.join(source_dir, file_name), destination_dir)
            print(
                f"Backup process finished successfully--> {date_and_time}", file=open(log_file, "a"))

# Check old files and delete if exists


def delete_old_files():
    for filename in os.listdir(source_dir):
        if filename.startswith("Thunder"):
            if os.path.getmtime(os.path.join(source_dir, filename)) < (now - (days * 86400)):
                if os.path.isfile(os.path.join(destination_dir, filename)):
                    print(filename)
                    os.remove(os.path.join(destination_dir, filename))
                    print(
                        f"Find files in the search. Olds files were deleted {filename}--> {date_and_time}", file=open(log_file, "a"))
            else:
                print(
                    f"Dont find files in the search. Dont delete olds backups --> {date_and_time}", file=open(log_file, "a"))


# Call Functions
if __name__ == '__main__':
    make_dir()
    make_compress()
    delete_old_files()
