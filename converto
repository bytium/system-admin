#!/bin/bash

## Just a simple script to convert any video to MOV that has user specified extension.
## After convert, the original file will be removed to save disk space!
## Edit it as needed


ext=$1
echo -e "\n1. First Navigate to the folder where mkv files are exis"
echo -e "2. Then Run converto to process all videos that has specified extension\n"
echo -e "example: converto mkv\n"
echo -e "Following video files will be converted to MOV:\n"

for i in $(ls *.$ext)
do
    echo -e "$i"
    filename=$(basename -- "$i")
    extension="${filename##*.}"
    filename="${filename%.*}"
    #echo $filename 
    if [ -f ${filename}_cvrtd.mov ]; then
                echo "${filename}_cvrtd.mov already exists."
                continue
    fi
    ffmpeg -y -i "$i"  -stats -hide_banner -loglevel panic -acodec pcm_s16le -vcodec copy "${filename}_cvrtd.mov"
    echo -e "\n$i has been converted! Now Deleting the old file to save disk space\n"
    rm "$i"
done
