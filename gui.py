import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog
import logic as lg
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.pyplot import figure


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        lg.names_params()


        # Grid configure
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        #self.columnconfigure(4, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        # Title
        self.title('ERSA config analizer')
        self.geometry('600x400')
        self.resizable(True, True)
        
        #Top label
        self.label = ttk.Label(self, text="Select mode")
        self.label.grid(row=0, column=0)

        # Modes for Combobox
        self.selected_mode = tk.StringVar()
        modes = ('SPC analysis', 'Check config', 'Compare graphs')

        # Mode Combobox
        self.mode_cb = ttk.Combobox(self, textvariable=self.selected_mode)
        self.mode_cb['values'] = modes
        self.mode_cb['state'] = 'readonly'
        self.mode_cb.grid(row=0, column=1, columnspan=2)
        self.mode_cb.bind('<<ComboboxSelected>>', self.bind_mode)

        # Browse button
        self.browse= ttk.Button(self, text="Browse")
        self.browse['command'] = self.browse_button
        self.browse.grid(row=1, column=0)

        # Select files button
        self.select = ttk.Button(self, text="Select Files")
        self.select['command'] = self.select_button
        self.select.grid(row=1, column=1)
        self.flag = 0

        # Run button
        self.run = ttk.Button(self, text="Run")
        self.run['command'] = self.run_button
        self.run.grid(row=1, column=2)

        # Path label
        self.path_l = ttk.Label(self, text="Path:")
        self.path_l.grid(row=2, column=0)

        # Path
        self.folder_path = tk.StringVar()
        self.path_name = ttk.Label(self, textvariable=self.folder_path)
        self.path_name.grid(row=3 ,column=0, columnspan=2, sticky=tk.W)

        list_of_configs = []
        self.log_var = tk.StringVar(value=list_of_configs)
        
        # Listbox
        self.listbox = tk.Listbox(self, listvariable=self.log_var, height=10, selectmode='extended')
        self.listbox.grid(row=4 ,column=0, columnspan=3, sticky=tk.EW)
        self.listbox.bind('<<ListboxSelect>>', self.bind_list)

        # Names of params
        hname = lg.hname
        self.chk_val = tk.StringVar(value=hname)

        # Lisbox of params
        self.listbox2 = tk.Listbox(self, listvariable=self.chk_val, height=10, selectmode='extended')
        self.listbox2.grid(row=4 ,column=3, columnspan=3, sticky=tk.EW)
        self.listbox2.bind('<<ListboxSelect>>', self.bind_list_of_params)
        
        # Select files button
        self.run = ttk.Button(self, text="Select files")
        self.run['command'] = self.select_files
        self.run.grid(row=5, column=1)

        # Select params button
        self.run = ttk.Button(self, text="Select params")
        self.run['command'] = self.select_params
        self.run.grid(row=5, column=4)




    def bind_mode(self, event):
        global sel_mode
        sel_mode = self.selected_mode.get()


    def browse_button(self):
        # Allow user to select a directory and store it in global val
        # Called folder_path
        global folder_path
        global file_dir
        global list_of_logs
        file_dir = tk.filedialog.askdirectory()
        self.folder_path.set(file_dir)
        self.flag = 1


    def select_button(self):
        global path_to_files, filenames 
        if self.flag and file_dir: 
            filetypes = (('XML Config files','*.xml_konf'),('text files', '*.txt'),('All files', '*.*')) #variants for formats

            path_to_files = tk.filedialog.askopenfilenames(title='Open files', initialdir=file_dir, filetypes=filetypes)
            filenames = []
            for p in path_to_files:
                p = p[(len(file_dir)+1):]
                filenames.append(p)
            self.log_var.set(filenames)
            

        else:
            self.folder_path.set("No directory chosen!")

    def bind_list(self, event):
        selected = self.listbox.curselection()
        global selected_logs
        selected_logs = [file_dir + '/' + self.listbox.get(i) for i in selected]

    def bind_list_of_params(self, event):
        selected = self.listbox2.curselection()
        global selected_params
        selected_params = [self.listbox2.get(i) for i in selected]

    def select_files(self):
        global configs
        configs = selected_logs

    def select_params(self):
        global parameters
        parameters = selected_params
        pass

    def run_button(self):
        sm = self.selected_mode.get()
        if sm == 'SPC analysis':
            #print('Selected params \n', selected_params)
            lg.get_all_files(configs, parameters)
            #print(parameters)
            #print(data_list)
            lg.graphs_drawing(parameters)
            print("Done!")


        elif sm == 'Check config':
            lg.get_all_files(configs, parameters)
            lg.save_data_to_txt(parameters)
            print("Done!")

        elif sm == 'Compare graphs':
            lg.get_all_files(configs, parameters)
            
            

        else:
            print("No mode chosen!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
