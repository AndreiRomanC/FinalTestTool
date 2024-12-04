#! /usr/bin/env python3
import tkinter as tk
import act
import ResourceManager
#from tkinterdnd2 import TkinterDnD
import memory_overwite
import file_utils
import config
import settings
import ch51
import ch52

import ch11
import ch12
import ch241
import ch421
import ch423
import ch25
import ch26
import a2lTotext
import a2lck_12
import a2lck_22
#import a2lck_1_2
#import PNGinPDF
import save
import ptuClean
import import_json
import Cbd_update_ptu
#import pyautogui 
#def browse_file():
 #   file_path = filedialog.askopenfilename()
 #   if file_path:
 #      # file_path_label.config(text=f"Fișier selectat: {file_path}")




def main(root):
    global project_path

    ResourceManager.clear_widgets(root)
    grid_container = tk.Frame(root)
    label_title = tk.Label(grid_container, text="Project Information",**settings.label_properties_title)
    root.title("Project information")
    print(f"Main execution")
    #entry_path_prj = tk.Entry(grid_container, width=70)
    #entry_path_prj.insert(0, config.project_path)  # Setați valoarea implicită
    #folder_path_label = tk.Label(grid_container, text="Project path selection", wraplength=400)
    #proj_path_button = tk.Button(grid_container, text="Browse", command=lambda:file_utils.browse_proj_folder(entry_path_prj))
    bt_normal = ResourceManager.add_browse_button(grid_container,config.work_path,"Work path: ",grid_container,row_p = 4,column_p = 0, padx_p = 0,pady_p=5,glb="work_path",en = "")
    ab = bt_normal
    bt_project_path = ResourceManager.add_browse_button(grid_container,config.project_path,"Project path: ",grid_container,row_p = 3,column_p = 0, padx_p = 0,pady_p=5,glb="project_path", en = ab)

    # Create a label to display the path of the selected file

    #print(f"Project path: {config.project_path}")

    
    ## Setting up the layout for the graphical interface elements

    label_title.grid(row=0, column=0, columnspan=3, padx=0, pady=(20, 20), sticky="ew")
    #folder_path_label.grid(row=1, column=0, padx=0, pady=0, sticky="w")
    #entry_path_prj.grid(row=1, column=1, padx=0, pady=0, sticky="w")
    #proj_path_button.grid(row=1, column=2, padx=0, pady=0, sticky="w")

    ResourceManager.add_ims_link(root,"Realization Order",config.ft_RO,grid_container,7,0,0,5,glb="config.ft_RO")
    ResourceManager.add_ims_link(root,"Test Session",config.ft_TS,grid_container,8,0,0,5,glb="config.ft_TS")

    ResourceManager.add_link(root,"Final test plan document sharpoint",config.ft_doc_link,grid_container,9,0,0,5)

    ResourceManager.add_file_browse_button(root,config.integration_manual_path,"Integration manual",grid_container,row_p = 10, column_p = 0, padx_p = 0, pady_p=5, open_option = 1)
    ResourceManager.add_file_browse_button(root,config.analyzed_logs,"Analyzed logs",grid_container,row_p = 11, column_p = 0, padx_p = 0, pady_p=5, open_option = 1)
    ResourceManager.add_browse_button(grid_container,config.ft_results,"FT Results: ",grid_container,row_p = 12,column_p = 0, padx_p = 0,pady_p=5,glb="work_path",en = "")



 
    #ResourceManager.add_ims_command(root,config.integration_manual_path,"IMS Realization Order",grid_container,row_p = 3,column_p = 0, padx_p = 5,pady_p=5, open_option = 1)

    grid_container.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
    root.grid_columnconfigure(0, weight=1,uniform="col")


root = tk.Tk()
root.title("Final Test Tool")

settings.set_window_size(root, 0.7, 0.7)


menu_bar = tk.Menu(root)

# Crearea unui meniu principal (primul meniu în bara de sus)
file_menu = tk.Menu(menu_bar, tearoff=0)  # tearoff=0 To prevent the detachment of the menu

# Adding options to the main menu
file_menu.add_command(label="Home", command=lambda:main(root))
file_menu.add_separator()  # Separator between options.
#file_menu.add_command(label="Test", command=lambda:act.main_act(root))
#file_menu.add_separator()  # Separator between options.
file_menu.add_command(label="Save", command=lambda:save.main_0(root))
file_menu.add_separator()  # Separator între opțiun
file_menu.add_command(label="Save as", command=lambda:save.save_as(root))
file_menu.add_separator()  # Separator între opțiun
file_menu.add_command(label="Import", command=lambda:[import_json.main_0(root),ResourceManager.clear_widgets(root), main(root)])
file_menu.add_separator()  # Separator între opțiun
file_menu.add_command(label="Exit", command=root.quit)

Chp1 = tk.Menu(menu_bar, tearoff=0)  # tearoff=0 To prevent the detachment of the menu
Chp1.add_command(label="1.1.1 & 1.1.2 - Missing and wrong ff configuration", command=lambda:ch11.main_0(root))
Chp1.add_separator()  # Separator between options.
Chp1.add_command(label="1.2.1 & 1.2.2 - Check for missing or wrong similar conditions configuration", command=lambda:ch12.main_0(root))

Chp2 = tk.Menu(menu_bar, tearoff=0)  # tearoff=0 To prevent the detachment of the menu
Chp2.add_command(label="2.4.1 - Check for wrong cbd files", command=lambda:ch241.main_0(root))
Chp2.add_separator()  # Separator between options.
Chp2.add_command(label="2.5 - Check for log warnings ", command=lambda:ch25.main_0(root))
Chp2.add_separator()  # Separator between options.
Chp2.add_command(label="2.6 Check the project configuration", command=lambda:ch26.main_0(root))


Chp4 = tk.Menu(menu_bar, tearoff=0)  # tearoff=0 To prevent the detachment of the menu
Chp4.add_command(label="4.2.1 Check the inputs for ENVD configuration", command=lambda:ch421.main_0(root))
Chp4.add_separator()  # Separator between options.
Chp4.add_command(label="4.2.3 Check correct access to array elements", command=lambda:ch423.main_0(root))
Chp4.add_separator()  # Separator between options.
Chp4.add_command(label="4.2.4 - Memory Overwrite", command=lambda:memory_overwite.main_0(root))

Chp5 = tk.Menu(menu_bar, tearoff=0)  # tearoff=0 To prevent the detachment of the menu
Chp5.add_command(label="5.1 - Run parse.py tool", command=lambda:ch51.main_0(root))
Chp5.add_separator()  # Separator between options.
Chp5.add_command(label="5.2 - No mapping of error indexes shall exist", command=lambda:ch52.main_0(root))


Ut = tk.Menu(menu_bar, tearoff=0)  # tearoff=0 To prevent the detachment of the menu
Ut.add_command(label="PTU Cleaner", command=lambda:ptuClean.main_0(root))
Ut.add_separator()  # Separator between options.
Ut.add_command(label="Cbd_update_ptu", command=lambda:Cbd_update_ptu.main_0(root))
Ut.add_separator()  # Separator between options.
Ut.add_command(label="A2l to text", command=lambda:a2lTotext.main_0(root))
Ut.add_separator()  # Separator between options.
#Ut.add_command(label="A2l check pt.1", command=lambda:a2lck_1.main_0(root))
#Ut.add_separator()  # Separator between options.
Ut.add_command(label="A2l check doc 1.DEM refactor config", command=lambda:a2lck_12.main_0(root))
Ut.add_separator()  # Separator between options.
Ut.add_command(label="A2l check doc 2.FIM refactor config", command=lambda:a2lck_22.main_0(root))
#Ut.add_command(label="PNGtoPDF", command=lambda:PNGinPDF.main_0(root))

# Adding the main menu to the top bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Chapter 1", menu=Chp1)
menu_bar.add_cascade(label="Chapter 2", menu=Chp2)
menu_bar.add_cascade(label="Chapter 4", menu=Chp4)
menu_bar.add_cascade(label="Chapter 5", menu=Chp5)

menu_bar.add_cascade(label="Utility Panel", menu=Ut)

root.config(menu=menu_bar)
main(root)



# Starting the main loop of the graphical interface
root.mainloop()
