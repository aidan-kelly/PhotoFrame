import time
import os
from tkinter import *
from PIL import Image, ImageTk
import downloader
import schedule

PHOTO_DIR = "/Users/aidankelly/Programming/photoframe/pics"
PHOTO_DURRATION = 15

#returns a label that contains the new image
def change_img(path_to_img, root, maxsize):

	#load the passed in image
	load = Image.open(path_to_img)
	load.thumbnail(maxsize, Image.ANTIALIAS)

	#convert to work with Tk
	render = ImageTk.PhotoImage(load)
	img = Label(root, image=render)
	img.image = render

	#center the label and return
	img.place(relx=.5, rely=.5, anchor="center")
	return img

def main():

	schedule.every().day.at("05:00").do(downloader.main)

	root = Tk()
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	maxsize = (screen_width-5, screen_height-5)


	root.wm_title("Photoframe")
	root.attributes('-fullscreen', True)
	root.configure(background="gray6")
	

	#loop through our pictures
	while True:
		schedule.run_pending()
		photo_list = os.listdir(PHOTO_DIR)

		for photo in photo_list:
			if(photo.endswith(".jpeg") or photo.endswith(".png") or photo.endswith(".jpg")):
				app = change_img((PHOTO_DIR + "/" + photo), root, maxsize)
				root.update_idletasks()
				root.update()
				time.sleep(PHOTO_DURRATION)
				app.destroy()
				root.update_idletasks()
				root.update()

if __name__ == '__main__':
    main()