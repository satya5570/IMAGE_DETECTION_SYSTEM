from tkinter import *
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


from _path_config import original_image_dataset_xlsx_path
from _path_config import chart_img_excel_file_path
import random

from tkinter import filedialog

# Mach Threshold
THRESHOLD = 83



def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)  # add this


# # condition will check true or false

def checkSimilarity(window, original_path_list, sample_path):
   
    result1 = match1(original_path_list, sample_path)  #sending 2 dimensional data to the signature 3 file
    #here result1 is also a 2d percent list
    # print("\n\n result1= ",result1)   #it is the unmodified list that fetchetd from Match_CNN_1 file  and in natural order
    for i in range(len(result1)):
        for j in range(len(result1[0])):

            if(result1[i][0]>100):
                result1[i][0]=100
            else:
                result1[i][0]=result1[i][0]+5

    result2_percent_col=[]
    for i in range(len(result1)):
        result2_percent_col.append(result1[i][0])

    result3_name_col=[]
    for i in range(len(result1)):
        result3_name_col.append(result1[i][1])

    print(result2_percent_col)
    name_of_img =""
    name_of_img_list =[]
    img_index_list=[]

    for i in range(len(result1)):
        for j in range(len(result1[0])):

            if(result1[i][0] >= THRESHOLD):
                name_of_img =result1[i][1]
                if(name_of_img not in name_of_img_list):
                    name_of_img_list.append(name_of_img)
                    img_index_list.append(i)
    print(name_of_img_list)
    print(img_index_list)
            

    strr=""
    if(len(name_of_img_list) > 0):
        strr="Match Found ! sample image is having "+str(len(name_of_img_list))+" names. \n Here are the names \n "+ str(name_of_img_list)
        
    else:
        strr="No Match Found in original database"

    print(len(name_of_img_list))
    print(strr)
 
    messagebox.showinfo("Match result", strr)


    print(max(result2_percent_col))

  

    # Create figures and plots

    chart_paths=[]
    sample_img_percent=100

    
    x = result3_name_col
    y = result2_percent_col

    # plt.plot(x, y,  color=['blue','red'])
    # plt.plot(x, y, color='gray')
    colors = ['red', 'green', 'blue', 'orange']
    plt.plot(x, y, color='gray')
    for i in range(len(result3_name_col)):
        plt.plot(result3_name_col[i], result2_percent_col[i], marker='o', color=colors[random.randint(0, 3)], linewidth=2, markersize=8)
    
    plt.title(f"Match Chart")
    plt.xlabel("images provided")
    plt.ylabel("similarity value of original")
    
    chart_path = f'C:/Users/satya/OneDrive/Desktop/IMAGE_DETECTION_SYSTEM/chartfolder/Match_Chart.png'
    plt.savefig(chart_path)
    chart_paths.append(chart_path)

    # Store chart paths in an Excel file
    df = pd.DataFrame({'Chart Path': chart_paths})

    # Write DataFrame to Excel file
    excel_file = 'C:/Users/satya/OneDrive/Desktop/IMAGE_DETECTION_SYSTEM/chart_imgs.xlsx'
    df.to_excel(excel_file, index=False)

    # Show all the figures
    plt.show()


  


    # Read the CSV file into a pandas DataFrame
    df1 = pd.read_excel(chart_img_excel_file_path)
    #print(df1)

    chart_img_paths = df1.values.tolist()

    # #print the new list
    print(chart_img_paths)


# Function to clear the Excel file
def clear_excel_file():
    file_path = original_image_dataset_xlsx_path
    if os.path.exists(file_path):
        df = pd.DataFrame()
        df.to_excel(file_path, index=False, engine='openpyxl')
        #print("Excel file cleared successfully.")



root = tk.Tk()
root.title("image Matching and detection")
root.geometry("1000x500") 

# Styling
bg_color = "#f0f0f0"
button_bg_color = "#4CAF50"
button_text_color = "white"
label_text_color = "black"
font_style = "Helvetica"

root.config(bg=bg_color)

uname_label = tk.Label(root, text="Compare image and detect", font=(font_style, 24, "bold"), bg=bg_color, fg=label_text_color)
uname_label.place(x=10, y=20)

img1_message = tk.Label(root, text="Sample Image", font=(font_style, 16), bg=bg_color, fg=label_text_color)
img1_message.place(x=10, y=100)
image1_path_entry = tk.Entry(root, font=(font_style, 14))
image1_path_entry.place(x=300, y=100, width=400, height=30)

img1_browse_button = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image1_path_entry))
img1_browse_button.place(x=720, y=100, width=100, height=30)



compare_button = tk.Button(root, text="Compare", font=(font_style, 18), bg="#008CBA", fg="white", command=lambda: read_excel_file(image1_path_entry.get()))
compare_button.place(x=400, y=180, width=150, height=45)



#############only read the excel data set and check similarity fucntion call###################
def read_excel_file(sample_path):
    # Read the CSV file into a pandas DataFrame
    sample_img_path=sample_path

    df = pd.read_excel(original_image_dataset_xlsx_path)
    #print(df)

    original_path = df.values.tolist()

    # #print the new list
    #print(original_path)
    #print(sample_img_path)
    checkSimilarity(root, original_path, sample_img_path)




root.mainloop()