from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import font
import os
import pandas as pd
import numpy as np
from numpy import result_type
from _path_config import original_image_dataset_xlsx_path
from _path_config import chart_img_excel_file_path
from tkinter import filedialog


def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)  # add this



# Function to clear the Excel file
def clear_excel_file():
    file_path = original_image_dataset_xlsx_path
    if os.path.exists(file_path):
        df = pd.DataFrame()
        df.to_excel(file_path, index=False, engine='openpyxl')
        print("Excel file cleared successfully.")


# def show_additional_fields():
    
#     # Additional fields
#     additional_img_label1 = tk.Label(root, text="Sitting position", font=(font_style, 16), bg=bg_color, fg=label_text_color)
#     image_original_name_entry = tk.Entry(root, font=(font_style, 14))

#     additional_img_label2 = tk.Label(root, text="Standing position", font=(font_style, 16), bg=bg_color, fg=label_text_color)
#     image3_path_entry = tk.Entry(root, font=(font_style, 14))

#     additional_img_label3 = tk.Label(root, text="Sleeping position", font=(font_style, 16), bg=bg_color, fg=label_text_color)
#     image4_path_entry = tk.Entry(root, font=(font_style, 14))

#     additional_img_label4 = tk.Label(root, text="Walking position", font=(font_style, 16), bg=bg_color, fg=label_text_color)
#     image5_path_entry = tk.Entry(root, font=(font_style, 14))

#     additional_browse_button1 = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image_original_name_entry))
#     additional_browse_button2 = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image3_path_entry))
#     additional_browse_button3 = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image4_path_entry))
#     additional_browse_button4 = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image5_path_entry))


#     # Show additional fields and browse buttons
#     additional_img_label1.place(x=10, y=320)
#     image_original_name_entry.place(x=300, y=320, width=400, height=30)
#     additional_browse_button1.place(x=720, y=320, width=100, height=30)

#     additional_img_label2.place(x=10, y=380)
#     image3_path_entry.place(x=300, y=380, width=400, height=30)
#     additional_browse_button2.place(x=720, y=380, width=100, height=30)

#     additional_img_label3.place(x=10, y=440)
#     image4_path_entry.place(x=300, y=440, width=400, height=30)
#     additional_browse_button3.place(x=720, y=440, width=100, height=30)

#     additional_img_label4.place(x=10, y=500)
#     image5_path_entry.place(x=300, y=500, width=400, height=30)
#     additional_browse_button4.place(x=720, y=500, width=100, height=30)
    
    
#     compare_button = tk.Button(root, text="Compare", font=(font_style, 18), bg="#008CBA", fg="white",command=lambda: readexcelfile())
#     compare_button.place(x=550, y=570, width=200, height=50)  # Show the Compare button






root = tk.Tk()
root.title("image Matching")
root.geometry("1000x700") 

# Styling
bg_color = "#f0f0f0"
button_bg_color = "#4CAF50"
button_text_color = "white"
label_text_color = "black"
font_style = "Helvetica"

root.config(bg=bg_color)

uname_label = tk.Label(root, text="Take input to original images dataset", font=(font_style, 24, "bold"), bg=bg_color, fg=label_text_color)
uname_label.place(x=10, y=20)

original_img_message = tk.Label(root, text="Original image path", font=(font_style, 16), bg=bg_color, fg=label_text_color)
original_img_message.place(x=10, y=100)

original_image_path_entry = tk.Entry(root, font=(font_style, 14))
original_image_path_entry.place(x=300, y=100, width=400, height=30)

original_image_browse_button = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=original_image_path_entry))
original_image_browse_button.place(x=720, y=100, width=100, height=30)

image_name_label = tk.Label(root, text="image original name", font=(font_style, 16), bg=bg_color, fg=label_text_color)
image_name_label.place(x=10, y=170)

image_original_name_entry = tk.Entry(root, font=(font_style, 14))
image_original_name_entry.place(x=300, y=170, width=400, height=30)

# img2_browse_button = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=sample_img_path))
# img2_browse_button.place(x=720, y=170, width=100, height=30)


# compare_button = tk.Button(root, text="Compare", font=(font_style, 18), bg="#008CBA", fg="white", command=lambda: checkSimilarity2(window=root,path1=original_image_path_entry.get(),path2=sample_img_path.get()))
# compare_button.place(x=400, y=240, width=150, height=45)


store_excel_button = tk.Button(root, text="store excel", font=(font_style, 18), bg=button_bg_color, fg="white",command=lambda: store_to_excel(original_image_path_entry.get(),image_original_name_entry.get()))
store_excel_button.place(x=250, y=570, width=200, height=50)  # Show the Compare button

clear_button = tk.Button(root, text="Clear Excel", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=clear_excel_file)
clear_button.place(x=550, y=570, width=200, height=50)




# #############only read the excel data set and check similarity fucntion call###################
# def readexcelfile():
#     # Read the CSV file into a pandas DataFrame
#     df = pd.read_excel(original_image_dataset_xlsx_path)
#     print(df)

#     original_path = df.values.tolist()

#     # Print the new list
#     print(original_path)
#     checkSimilarity(window=root,path=original_path)


##################################from here only excel works##################
def store_to_excel(path1,imgname):
    path1 = original_image_path_entry.get()
    original_path=[path1,imgname]
    write_to_excel(original_path)

def write_to_excel(original_path):
    file_path = original_image_dataset_xlsx_path

    # Check if the file already exists
    if os.path.exists(file_path):
        # Read existing data
        df = pd.read_excel(file_path)
        # Create a new DataFrame from the original_path
        new_data = pd.DataFrame([original_path])
        # Concatenate the existing DataFrame with the new DataFrame
        df = pd.concat([df, new_data], ignore_index=False)
    else:
        # Create new DataFrame if the file doesn't exist
        df = pd.DataFrame([original_path])
    
    # Write the DataFrame to the Excel file
    df.to_excel(file_path, index=False, engine='openpyxl')
    print("Data stored successfully in '{}'".format(file_path))


root.mainloop()