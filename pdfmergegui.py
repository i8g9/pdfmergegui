from tkinter import font
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileMerger

root = tk.Tk()
root.title('PDF Merger')

canvas1 = tk.Canvas(root, width = 300, height = 430 ,bg='black' ,relief = 'flat')
canvas1.pack()

label1 = tk.Label(root, text='PDF Merger' ,bg='black' ,fg='white')
label1.config(font=('helvetica', 18))
canvas1.create_window(150, 60, window=label1)

#Open PDF 1 Function
def openFile1():
    global pdf1

    import_file_path = filedialog.askopenfilename(initialdir = "/", title = "Select a PDF", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    pdf1 = import_file_path

    label2 = tk.Label(root, text='loaded', bg='black',fg='white')
    label2.config(font=('helvetica', 12))
    canvas1.create_window(40, 130, window=label2)

#Open PDF 1 Button
browseButton = tk.Button(text="     Select File     ",bg='purple1', fg='white' ,command=openFile1, font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(150, 130, window=browseButton)

#Open PDF 2 Function
def openFile2():
    global pdf2

    import_file_path = filedialog.askopenfilename(initialdir = "/", title = "Select a PDF", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    pdf2 = import_file_path

    label3 = tk.Label(root, text='loaded', bg='black',fg='white')
    label3.config(font=('helvetica', 12))
    canvas1.create_window(40, 170, window=label3)

#Open PDF 2 Button
browseButton = tk.Button(text="     Select File     ",bg='purple1', fg='white' ,command=openFile2, font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(150, 170, window=browseButton)

#Open PDF 3 Function
def openFile3():
    global pdf3

    import_file_path = filedialog.askopenfilename(initialdir = "/", title = "Select a PDF", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    pdf3 = import_file_path

    label4 = tk.Label(root, text='loaded', bg='black',fg='white')
    label4.config(font=('helvetica', 12))
    canvas1.create_window(40, 210, window=label4)

#Open PDF 3 Button
browseButton = tk.Button(text="     Select File     ",bg='purple1', fg='white' ,command=openFile3, font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(150, 210, window=browseButton)

#Open PDF 4 Function
def openFile4():
    global pdf4

    import_file_path = filedialog.askopenfilename(initialdir = "/", title = "Select a PDF", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    pdf4 = import_file_path

    label5 = tk.Label(root, text='loaded', bg='black',fg='white')
    label5.config(font=('helvetica', 12))
    canvas1.create_window(40, 250, window=label5)

#Open PDF 4 Button
browseButton = tk.Button(text="     Select File     ",bg='purple1', fg='white' ,command=openFile4, font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(150, 250, window=browseButton)

#Open PDF 5 Function
def openFile5():
    global pdf5

    import_file_path = filedialog.askopenfilename(initialdir = "/", title = "Select a PDF", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    pdf5 = import_file_path

    label6 = tk.Label(root, text='loaded', bg='black',fg='white')
    label6.config(font=('helvetica', 12))
    canvas1.create_window(40, 290, window=label6)

#Open PDF 5 Button
browseButton = tk.Button(text="     Select File     ",bg='purple1', fg='white' ,command=openFile5, font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(150, 290, window=browseButton)

#Combine PDFs Function
def convertFile():
    global pdfs
    pdfs = [pdf1, pdf2, pdf3, pdf4, pdf5]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)
    
    merger.write("result.pdf")

# Save File Button
saveAsButton = tk.Button(text="Convert to PDF", bg="purple1", fg="white",command=convertFile ,font=("helvetica", 12, "bold"), relief="flat")
canvas1.create_window(150, 330, window=saveAsButton)

#Exit Application Function
def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application','Are you sure you want to exit the application?',icon = 'warning')
    if MsgBox == 'yes':
        root.destroy()

#Exit Application Function
exitButton = tk.Button(text="Exit Application", bg="black", fg="white", command=exitApplication, font=("helvetica", 12, "bold"), relief="flat")
canvas1.create_window(150, 370, window=exitButton)

root.mainloop()
