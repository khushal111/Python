import os
import random

def rename_files():
    # (1)  get file names from a folder
    
    file_list = os.listdir(r"C:\Users\rajawatk\Downloads\Python Practice\alphabet")
   # print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\rajawatk\Downloads\Python Practice\alphabet")

    # (2)  for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        file_name = str(random.randint(1,99)) + file_name
        os.rename(file_name, file_name.translate(None, "0123456789"))
        
           
    os.chdir(saved_path)

rename_files(r"C:\Users\rajawatk\Downloads\Python Practice\alphabet")
