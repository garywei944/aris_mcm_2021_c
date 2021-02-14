#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clip_videos.py
# @Date    : 02/07/2021
# @Author  : garywei944 (garywei944@gmail.com)
# @Link    : https://github.com/garywei944

# This script is modified from https://blog.csdn.net/y459541195/article/details/100687966

import torch

import sys
import os
import shutil
import argparse
import logging
from pathlib import Path

parser = argparse.ArgumentParser(
    description='Split the files under input directory into training set and validation set with 8:2 ratio')
parser.add_argument('-i', '--input', type=str, required=True)

logging.basicConfig(level=logging.INFO, stream=sys.stderr)

if __name__ == "__main__":
    args = parser.parse_args()

    input_path = Path(args.input)

    file_list = os.listdir(input_path)
    train_size = int(len(file_list) * 0.8)
    val_size = len(file_list) - train_size

    train_set, val_set = torch.utils.data.random_split(file_list, [train_size, val_size])

    (input_path / 'train').mkdir(parents=True, exist_ok=True)
    (input_path / 'val').mkdir(parents=True, exist_ok=True)

    for files in train_set:
        shutil.move(str(input_path / files), str(input_path / 'train'))
    for files in val_set:
        shutil.move(str(input_path / files), str(input_path / 'val'))
