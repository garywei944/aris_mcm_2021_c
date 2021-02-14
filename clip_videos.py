#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clip_videos.py
# @Date    : 02/07/2021

# This script is modified from https://blog.csdn.net/y459541195/article/details/100687966

import cv2

import sys
import os
import argparse
import logging
from pathlib import Path

parser = argparse.ArgumentParser(
    description='Make a screenshot to all videos in input dir and output to the output dir')
parser.add_argument('-i', '--input', type=str, required=True)
parser.add_argument('-o', '--output', type=str, required=True)

logging.basicConfig(level=logging.INFO, stream=sys.stderr)

if __name__ == "__main__":
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)

    for files in os.listdir(input_path):
        file_name = os.path.splitext(files)[0]

        logging.info("Processing {}".format(input_path / files))
        video = cv2.VideoCapture(str(input_path / files))

        # Read one frame in case of error
        video.read()

        success = True
        i, j = 0, 0
        while success:
            success, frame = video.read()
            if i % 150 == 0:
                logging.info("Saving {} frame {}".format(input_path / files, i))
                cv2.imwrite(str(output_path / "{}_clip_{}.png".format(file_name, j)), frame)
                j += 1
            i += 1
