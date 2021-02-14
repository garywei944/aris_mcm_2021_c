#!/bin/bash

# Move data to sub folders according to their file type
#bash ./process_images.sh

# Resize all images to 416*416
mkdir data
python resize_images.py -i "2021MCM_ProblemC_Files/images" -o "data"

# Make a clip every 150 frames and resize it to 416*416
#mkdir -p 2021MCM_ProblemC_Files/video_clips
#python clip_videos.py -i "2021MCM_ProblemC_Files/videos" -o "2021MCM_ProblemC_Files/video_clips"
python resize_images.py -i "2021MCM_ProblemC_Files/video_clips" -o "data"

# Copy the data folder to re-label everything
cp -ar data/ data_cp/

# Move images into sub-folders according to their Lab Status
python classify_images_into_subfolder.py -i "data"

mv data/1.0/* data/
mv data/0.0/* data/

rm -fr data/0.0 data/1.0 data/2.0

# Split into train set and val set with ratio 8:2
python split_train_and_val.py -i "data"

# Move images into sub-folders according to their Lab Status
python classify_images_into_subfolder.py -i "data/train"
python classify_images_into_subfolder.py -i "data/val"

