import tkinter as tk
from tkinter import filedialog,messagebox,ttk
from translate import Translate


translate=Translate("","","",[])

def get_files():
    files = filedialog.askopenfilenames(filetypes=[('text files', '.txt')])
    translate.file_paths=files
    if files:
        for file in files:
            text1.insert(tk.END, file + '\n')
            text1.update()
    else:
        print('you have not selected any files')
def set_result_path():
    result_path=filedialog.askdirectory()
    translate.result_root_path=result_path
    text2.insert(tk.END,result_path)
# def set_from_lang():
#     translate.trans_type[0]=""
# def set_to_lang():
#     translate.trans_type[1]=""
def translate_files():
    if translate.file_paths:
        translate.translate_files()
        tk.messagebox.showinfo("hint","get it done")
    else :
        tk.messagebox.showinfo("hint","no file")


root=tk.Tk()
root.title("Batchfile Translator")
frm = tk.Frame(root)
frm.grid(padx='50', pady='50')
# label1=tk.Label(frm,text="Select the file to be translated：")
# label1.grid(row=0,column=0)
btn_get_file = tk.Button(frm, text='Select the file to be translated', command=get_files)
btn_get_file.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
text1 = tk.Text(frm, width='40', height='10')
text1.grid(row=0, column=1)
btn_get_result_path=tk.Button(frm,text='Select translation result path',command=set_result_path)
btn_get_result_path.grid(row=1,column=0)
text2=tk.Text(frm,width='40', height='2')
text2.grid(row=1,column=1)

btn_sure=tk.Button(frm,text="translate",command=translate_files)
btn_sure.grid(row=2,column=1)


root.mainloop()
