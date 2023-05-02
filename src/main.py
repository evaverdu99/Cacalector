from model.App import *
from tkinter import *
from tkinter import filedialog
        
def main(): 
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Open the export chat to analise", filetypes=(("text    files","*.txt"), ("all files","*.*")))
    
    app = App(file_path)
    app.startApplication()
     
    print("end")
    

if __name__ == "__main__":
    main()