from tkinter import Tk,Button,PhotoImage,messagebox
import gc
import wget

gc.collect()

def Lock_call():
    if __name__ == "__main__":
        import data
        data.Lock()
    
def Unlock_call():
    if __name__ == "__main__":
        import data
        data.Unlock()
def up():
    try:
        url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
        wget.download(url,"Update.exe")
    except:
        messagebox.showinfo("Update","Update Not Found")
    
root = Tk()
root.title("FileEncrypt")
root.geometry("596x416")
root.resizable(False,False)
root.config(bg='#2D2929')

Lock_icon = PhotoImage(file='Lock.png')
Lock_icon_l = Button(root,image=Lock_icon,bg='#2D2929',border=0,activebackground='#2D2929',command=Lock_call).place(x=82,y=132)

UnLock_icon = PhotoImage(file='Unlock.png')
UnLock_icon_l = Button(root,image=UnLock_icon,bg='#2D2929',border=0,activebackground='#2D2929',command=Unlock_call).place(x=194,y=132)

Cloud_icon = PhotoImage(file='Backup.png')
Cloud_icon_l = Button(root,image=Cloud_icon,bg='#2D2929',border=0,activebackground='#2D2929').place(x=306,y=132)

Update_icon = PhotoImage(file='Update.png')
Update_icon_l = Button(root,image=Update_icon,bg='#2D2929',border=0,activebackground='#2D2929',command=up).place(x=418,y=132)

root.mainloop()


