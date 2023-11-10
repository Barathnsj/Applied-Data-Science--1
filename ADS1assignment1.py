# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:55:33 2023

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os 
print(os.getcwd)
new_directory_name = "tmp"

if not os.path.exists(new_directory_name):
    os.mkdir(new_directory_name)
if os.path.exists(new_directory_name):
    os.rmdir(new_directory_name)
    print(f"Removed the directory: {new_directory_name}")
final_directory_content = os.listdir(new_directory_name)
print("Final directory content:", final_directory_content)
