#!/bin/bash

# Process images

# 1. move png, jpg, and jfif files into the folder `images`
# 2. move mov and mp4 files into the folder 'video'

mkdir data

DIR=2021MCM_ProblemC_Files
cd $DIR || exit

mkdir images videos

mv ./*.png ./*.PNG ./*.jpg ./*.JPG ./*.jfif ./*.JFIF images/
mv ./*.mov ./*.MOV ./*.mp4 ./*.MP4 videos/
