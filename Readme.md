# IMAGE DETECTION SYSTEM

### About

provide sample image and match it with images in dataset wether it exists or not in dataset.
if exists then show its corresponding name of image

it will also help in detecting images with many different names

This uses CNN algorithm (Convolutional Nural Network)

### Requirements

from tkinter import \*
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import font
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import result_type
from Match_CNN_1 import match1

from \_path_config import original_image_dataset_xlsx_path
from \_path_config import chart_img_excel_file_path
from tkinter import filedialog

import cv2
from skimage.metrics import structural_similarity as ssim
import statistics

### how output will work or how to use

- first take the input in the field as image
  (browse the image path or put the image path in field)

- images should be in jpg, png, jpeg format

1. while run it will show the first ui inter face with 1 text input fields i.e. sample image path field (that what we want to know the image to be detected) and also there is 1 button named 'compare'.

2. on clicking compare button it will match the smpale image with all the images in original provided dataset and show output in a message box wehter images are similar or not.

3. onclicking the compare button it will check the images and match sample with each images in original dataset and it shows the maximum similarity holding image position in messesge box . and one more thing wether the images matched or not . (if result_value > THERESOLD VLAUE then matched otherwise not ; THERESOLD IS 83%)

4. then it will show the chart of matching images in dataset.

**NOTE**:

- first store some images and names to original_image_dataset.xlsx by using interface of storeto_orignal_image_dataset.py

### important files and folders

- main_match_img.py
- Match_CNN_1.py
- \_path_config.py
- storeto_orignal_image_dataset.py
- original_image_dataset.xlsx
- chart_imgs.xlsx
- Readme.md

- folders
  - chartfolder
  - images

### About developer

- **SATYANARAYANA SATAPATHY**
  E-MAIL: satyanarayanasatapathy65@gmail.com
