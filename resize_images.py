#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# resize_images.py
# @Date    : 02/07/2021
# @Author  : garywei944 (garywei944@gmail.com)
# @Link    : https://github.com/garywei944

# This script is modified from https://blog.csdn.net/y459541195/article/details/100687966

import cv2
import numpy as np

import sys
import os
import argparse
import logging
from pathlib import Path

parser = argparse.ArgumentParser(description='Resize all images in input dir to 416*416 and output to the output dir')
parser.add_argument('-i', '--input', type=str, required=True)
parser.add_argument('-o', '--output', type=str, required=True)

logging.basicConfig(level=logging.WARNING, stream=sys.stderr)


def resize_img(image_, target):
    target_h, target_w = target
    h, w, _ = image_.shape

    # Resize the original image to fit the target resolution
    scale = min(target_w / w, target_h / h)
    new_w, new_h = int(scale * w), int(scale * h)
    image_resized = cv2.resize(image_, (new_w, new_h))

    # Creat a canvas with target_h and target_w
    # fill_value=120 is Grey
    image_padded = np.full(shape=[target_h, target_w, 3], fill_value=120)
    d_w, d_h = (target_w - new_w) // 2, (target_h - new_h) // 2

    # Put the resized image into the middle of the canvas
    image_padded[d_h:new_h + d_h, d_w:new_w + d_w, :] = image_resized

    return image_padded


if __name__ == "__main__":
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)

    for files in os.listdir(input_path):
        file_name = os.path.splitext(files)[0]

        logging.info("Processing {}".format(input_path / files))
        image = cv2.imread(str(input_path / files))
        if image is None:
            continue
        img = resize_img(image, (416, 416))
        cv2.imwrite(str(output_path / "{}.png".format(file_name)), img)
