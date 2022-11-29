from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import os.path
from datetime import datetime 
import shutil

root = Tk()
root.geometry(r'400x500+700+300')
root.resizable(False, False)

root.title(r'Photosort')
# root.iconbitmap(r'C:\IT Tools\PyProjects\Compilation\Notepad\notepad.ico')

main_menu = Menu(root)
root.config(menu=main_menu)

def ps_select_output_folder():
    folder_path = filedialog.askdirectory(title=r'Select Output Photosort Directory', mustexist=TRUE)
    if folder_path:
        outputfolder_path_text['text'] = folder_path
        ps_addtext(r'Output folder(s) successfully selected...')

def ps_select_input_folder():
    folder_path = filedialog.askdirectory(title=r'Select Output Photosort Directory', mustexist=TRUE)
    if folder_path:
        inputfolder_path_text['text'] = folder_path
        ps_addtext(r'Input folder(s) successfully selected...')

def ps_exit():
    if messagebox.askokcancel(title=r'Exit PhotoSort', message=r'Are you sure to Exit PhotoSort?') == True:
        root.destroy()

def ps_sort(path):
    paths = [path + "/" + f_path for f_path in os.listdir(path)]
    for fdpath in paths:
        if os.path.isfile(fdpath) == False:
            ps_sort(fdpath)
        else:
            date = datetime.fromtimestamp(os.stat(fdpath).st_mtime)
            folder_date = date.strftime('%Y' + '-' + '%m' + '-' + '%d')
            input_folder = inputfolder_path_text['text'] + "\\" + folder_date
            if not os.path.exists(input_folder):
                os.makedirs(input_folder) 
            shutil.copy(fdpath, input_folder)
            ps_addtext(f'{fdpath} copied!')
    ps_addtext(r'Successfully Complited!')
                      
def ps_addtext(text):
    progress_text.config(state=NORMAL)
    progress_text.insert(END, f'{text}\n')
    progress_text.yview(END)
    progress_text.config(state=DISABLED)

# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label=r'Select Output Folder', command=lambda: ps_select_output_folder())
file_menu.add_command(label=r'Select Input Folder', command=lambda: ps_select_input_folder())
file_menu.add_separator()
file_menu.add_command(label=r'Exit PhotoSort', command=lambda: ps_exit())
main_menu.add_cascade(label=r'File', menu=file_menu)

# output frame
outputfolder_path_frame = ttk.LabelFrame(root, text=r'Selected Output PhotoSort Folder:')
outputfolder_path_frame.place(anchor=NW, rely=.01, relx=.03, height=45, relwidth=.94)
outputfolder_path_text = ttk.Label(outputfolder_path_frame, text=r'Not Selected, please Select in [FILE] menu')
outputfolder_path_text.place(anchor=NW, rely=.01, relx=.03, relwidth=.89)
get_output_folder_button = ttk.Button(outputfolder_path_frame, text=r' / ', command=lambda: ps_select_output_folder())
get_output_folder_button.place(anchor=SE, rely=.85, relx=.99, width=25)

# input frame
inputfolder_path_frame = ttk.LabelFrame(root, text=r'Selected Input PhotoSort Folder:')
inputfolder_path_frame.place(anchor=NW, rely=.11, relx=.03, height=45, relwidth=.94)
inputfolder_path_text = ttk.Label(inputfolder_path_frame, text=r'Not Selected, please Select in [FILE] menu')
inputfolder_path_text.place(anchor=NW, rely=.01, relx=.03, relwidth=.89)
get_input_folder_button = ttk.Button(inputfolder_path_frame, text=r' / ', command=lambda: ps_select_input_folder())
get_input_folder_button.place(anchor=SE, rely=.85, relx=.99, width=25)

# progress text field
progress_frame = ttk.LabelFrame(root, text=r'Progress Log:')
progress_frame.place(anchor=NW, rely=.21, relx=.03, height=340, relwidth=.94)
progress_text = Text(progress_frame, state=DISABLED, font=('Comic Sans MS', 10, 'italic'))
progress_text.place(relx=.5, rely=0, relheight=.98, relwidth=.95, anchor=N)


# main button
start_button = ttk.Button(root, text='Start', command=lambda: ps_sort(outputfolder_path_text['text']))
start_button.place(anchor=NW, rely=.91, relx=.03, height=35, relwidth=.94)

root.mainloop()