#!/bin/bash
PATH_SCRIPT=`dirname ${BASH_SOURCE[0]}`
DATE_Y_TIME=`date "+%d-%m-%y_%H-%M-%S"`
DATE=`date "+%d-%m-%y"`
FILE_NAME="Thunder_$DATE.tgz"
LINES=0
DEST_FOLDER="$PATH_SCRIPT/Bk_email_automatico"
# Note: You can change the folder to bk, if folder isnt in the path script, write absolute path
SOURCE_FOLDER="/home/user/.thunderbird"
# make directory 
make_dir()
{
  mkdir -p "$DEST_FOLDER"
}

# Check if file exists 
# Add log output to watch result of script
compress_files()
{
if [ -f /home/user/Documents/Bk_email_automatico/$FILE_NAME ];then
  echo "Dont create the file because it already exists-->  $DATE_Y_TIME" >> $DEST_FOLDER/log.txt;
  echo "Backup process finished with errors. See Logs"
else
# Package file with tar and add options  c for make, v is verbose mode, z to compress with gzip 
# And f to operate over the file   	
  tar cfvz "$DEST_FOLDER/$FILE_NAME" --absolute-names "$DEST_FOLDER";
  echo "Backup process finished susccessfully -->  $DATE_Y_TIME" >> $DEST_FOLDER/log.txt
fi
}
#Assign into LINES the rearch result, also with "wc -l" count the lines to compare later
LINES=$(find /home/user/Documents/Bk_email_automatico/Thunder* -mtime +14 | wc -l)

# Do the comparison and delete old files
delete_oldfiles()
{
if [ "$LINES" -eq 0  ]; then
  echo "Dont find files in the search . Dont delete olds backups -->  $DATE_Y_TIME" >> $DEST_FOLDER/log.txt;
else
  find /home/user/Documents/Bk_email_automatico/Thunder* -mtime +14 -delete;
  echo "Find files in the search. Olds files were delete -->  $DATE_Y_TIME" >> $DEST_FOLDER/log.txt;
fi
}

make_dir
compress_files
delete_oldfiles