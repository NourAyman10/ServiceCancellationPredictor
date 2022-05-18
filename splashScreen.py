import shutil
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
from home import Home


class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        # setting background image
        self.image = Image.open("Photos/background.png")
        self.backgroundImage = ImageTk.PhotoImage(self.image)
        self.backgroundLabel = Label(self.root, image=self.backgroundImage)

        self.main_frame = tk.Frame(self.root, borderwidth=0, background='#191142')

        self.image_label = tk.Label(self.main_frame, image="", borderwidth=0, background='#191142')

        self.logo = Image.open("Photos/logo.png")
        self.logoImage = ImageTk.PhotoImage(self.logo)
        self.logoLabel = Label(self.root, image=self.logoImage, background='#191142')

        self.loading = Image.open("Photos/loading.png")
        self.loadingImage = ImageTk.PhotoImage(self.loading)
        self.loadingLabel = Label(self.root, image=self.loadingImage, background='#191142')

        self.backgroundLabel.place(x=0, y=0)
        self.main_frame.place(anchor='center', relx=0.5, rely=0.45)
        self.logoLabel.place(anchor='center', relx=0.5, y=100)
        self.loadingLabel.place(anchor='center', relx=0.5, rely=0.87)
        self.image_label.pack()

        os.mkdir("gif_frames")

        self.start = time.time()
        self.gif_frames = []
        self.images = []
        self.animation()
        self.root.mainloop()

    def animation(self):
        gif = Image.open("Photos/gif1.gif")
        self.no_of_frames = gif.n_frames

        for i in range(self.no_of_frames):
            gif.seek(i)
            gif.save(os.path.join("gif_frames", f"gif{i}.png"))
            self.gif_frames.append(os.path.join("gif_frames", f"gif{i}.png"))

        for images in self.gif_frames:
            im = Image.open(images)
            im = im.resize((800, 650), Image.Resampling.LANCZOS)
            im = ImageTk.PhotoImage(im)
            self.images.append(im)

        self.show_animation(0)

    def show_animation(self, count):
        image = self.images[count]
        self.image_label.configure(image=image)
        count += 1
        if count == len(self.images) - 1:
            count = 0
        if (time.time() - self.start) <= 5:
            self.x = self.root.after(15, self.show_animation, count)
        elif (time.time() - self.start) > 5:
            self.root.destroy()
            shutil.rmtree('gif_frames')
            Home()


Screen()
