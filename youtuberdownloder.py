from pytube import YouTube
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog as fd



root = Tk()
root.geometry('500x300') # Size of the window
root.resizable(0, 0) # makes the window adjustable with its features
root.title('youtube downloader')
filetypes = ( ('text files', '*.txt'), ('All files', '*.*') )
folder_selected = ""
linkd = StringVar()
path = StringVar()

def download():
	if linkd.get() == "":
		messagebox.showinfo("path", "please enter link")
	elif folder_selected == "":
		messagebox.showinfo("path", "please select path")
	else:
		try:
			url = YouTube(str(linkd.get()))

			print() #This captures the link(url) and locates it from YouTube.
			video = url.streams.all()
 # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
			video[2].download(folder_selected) # This is the method with the instruction to download the video.
			Label(root, text="Downloaded!", font="arial 15",fg = "green").place(x=180, y=250)
		except:
			messagebox.showerror("error", "something went wrong!")
			
def pathh():
	global folder_selected
	folder_selected = fd.askdirectory()
Label(root, text="Download Youtube videos", font='san-serif 14 bold').pack()


Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=linkd).place(x=30, y=85)


Label(root, text="PATH to save the file", font='san-serif 15 bold').place(x=150, y=120)
Button(root, text='PATH', font='san-serif 14 bold', bg='white', padx=1,command=pathh).place(x=205, y=150)

Button(root, text='Download', font='san-serif 16 bold', bg='red', padx=2,command=download).place(x=180, y=200)
root.mainloop()

