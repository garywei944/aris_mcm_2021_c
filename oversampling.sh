#!/bin/bash

# Copy data_cp to data_oversampling and do oversampling
cp -ar data_cp/ data_oversampling/

python classify_images_into_subfolder.py -i "data_oversampling"

rm -fr data_oversampling/2.0

files=(data_oversampling/1.0/*.png)
NUM_P=${#files[@]}
files=(data_oversampling/0.0/*.png)
NUM_N=${#files[@]}

# Oversampling the positive data to make the ratio of training data 1:15
RATIO="$((NUM_N/15/NUM_P))"
for files in data_oversampling/1.0/*; do
  [[  -e "$files"  ]] || break
  for ((i=0; i<RATIO; i++)); do
    file_name=${files%.png}
    cp "${files}" "${file_name}_copy_${i}.png"
  done
done

mv data_oversampling/1.0/* data_oversampling/
mv data_oversampling/0.0/* data_oversampling/

rmdir data_oversampling/0.0 data_oversampling/1.0

# Split into train set and val set with ratio 8:2
python split_train_and_val.py -i "data_oversampling"

# Move images into sub-folders according to their Lab Status
python classify_images_into_subfolder.py -i "data_oversampling/train"
python classify_images_into_subfolder.py -i "data_oversampling/val"
