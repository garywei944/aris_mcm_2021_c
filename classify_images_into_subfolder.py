#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# classify_images_into_subfolder.py
# @Date    : 02/08/2021
# @Author  : garywei944 (garywei944@gmail.com)
# @Link    : https://github.com/garywei944

# This script is modified from https://blog.csdn.net/y459541195/article/details/100687966

import numpy as np
import pandas as pd
import cv2

from preprocess import load_and_process

import sys
import os
import argparse
import logging
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description='Move images into sub-folders according to their Lab Status')
parser.add_argument('-i', '--input', type=str, required=True)

logging.basicConfig(level=logging.WARNING, stream=sys.stderr)

if __name__ == "__main__":
    args = parser.parse_args()

    input_path = Path(args.input)

    data, image_id = load_and_process()

    # Make directories
    for dirs in data['Lab Status'].unique():
        dirs = str(dirs)
        (input_path / dirs).mkdir(parents=True, exist_ok=True)

    for files in os.listdir(input_path):
        if (input_path/files).is_dir():
            continue

        file_name = os.path.splitext(files)[0]

        # logging.info("Processing {}".format(input_path / files))

        # If the image is clipped from a video, the file_name does not match what records in image_id
        if file_name not in image_id['FileName'].values:
            file_name = file_name.split('_clip_')[0]
            file_name = file_name.split('_copy_')[0]

        global_id_list = image_id[image_id['FileName'] == file_name].index

        # logging the file_name if we cannot find the global id
        if global_id_list is None or len(global_id_list) == 0:
            logging.warning(file_name)
            continue
        global_id = global_id_list[0]
        label = str(data.loc[global_id, 'Lab Status'])

        # Move the file into according sub-folder
        shutil.move(str(input_path / files), str(input_path / label))
