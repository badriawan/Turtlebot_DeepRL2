# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches
import os

def filterFiles(directoryPath, extension):
    """
        This function filters the format files with the selected extension in the directory
        
        Args:
            directoryPath (str): relative path of the directory that contains text files
            extension (str): extension file

        Returns:
            The list of filtered files with the selected extension
    """    
    relevant_path = directoryPath
    included_extensions = [extension]
    file_names = [file1 for file1 in os.listdir(relevant_path) if any(file1.endswith(ext) for ext in included_extensions)]
    numberOfFiles = len(file_names)
    listParams = [file_names, numberOfFiles]
    return listParams

[image_names, numberOfFiles] = filterFiles("Thyroid/Data/Original Image/Benign", "jpg")    

print(image_names)