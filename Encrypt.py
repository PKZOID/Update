from tkinter import Frame, Button,Label,PhotoImage,Tk,messagebox,filedialog
import gc
import wget
import os
import pyAesCrypt

gc.collect()

store = "786"
counter = 0

root = Tk()
root.title("FileEncrypt")
root.geometry("596x416")
root.resizable(False,False)
photo = PhotoImage(file = "data//icon.png")
root.iconphoto(False,photo)

bg = PhotoImage(file='Background.png')
back = Label(root,image=bg).pack()

def Lock_call():
    if __name__ == "__main__":
        gc.collect()
        global in_path_dec
        global counter
        counter += 22
        in_path_dec = filedialog.askopenfilename()
        file_name = os.path.basename(in_path_dec)
        Label(root,text=file_name,bg='#519872',width=70,height=1).place(x=50,y=120+counter)
        Button(root,text="Encrypter",relief='groove',command=encrypt).place(x=90,y=120+counter)
        f = open("path.text",'w')
        f.write(in_path_dec+'\n')
        f.close()

def encrypt():
    f = open("path.text",'r')
    a = f.read()
    password = store
    pyAesCrypt.encryptFile(a,  a+".lock", password)
    messagebox.showinfo("File Locked", "Your File Has Been Locked")

def Unlock_call():
    if __name__ == "__main__":
        gc.collect()
        in_path_dec = filedialog.askopenfilename()
        new_name = os.path.splitext(in_path_dec)[0]
        password = store
        pyAesCrypt.decryptFile(in_path_dec, new_name, password)
        messagebox.showinfo("File Decrypted", "Your File Decrypted")

def up():
    if __name__ == "__main__":
        try:
            url = 'https://raw.githubusercontent.com/PKZOID/Update/main/Encrypt.py'
            wget.download(url,"Update.exe")
        except:
            messagebox.showinfo("Update","Update Not Found")

def backup():
    if __name__ == "__main__":
        messagebox.showinfo("Coming Soon", "Cloud Backup Feature")

drop = PhotoImage(file='dropbox.png')
drop_box = Button(root,image=drop,bg='#ebeee6',border=0,activebackground='#ebeee6',cursor='hand2',command=encrypt).place(x=188,y=80)

git = PhotoImage(file='githab.png')
git_ic = Button(root,image=git,bg='#ebeee6',border=0,activebackground='#ebeee6',cursor='hand2',command=Unlock_call).place(x=268,y=80)

gitub = PhotoImage(file='gitlab.png')
git_lab = Button(root,image=gitub,bg='#ebeee6',border=0,activebackground='#ebeee6',cursor='hand2',command=backup).place(x=348,y=80)

Upload = PhotoImage(file='Upload.png')
upload_btn = Button(root,image=Upload,bg='#ebeee6',border=0,activebackground='#ebeee6',cursor='hand2',command=Lock_call).place(x=225,y=22)

root.mainloop()


