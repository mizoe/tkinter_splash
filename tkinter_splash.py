import tkinter
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.geometry("0x0")
        self.open_splash_window()

    def open_splash_window(self):
        self.splash_window = tkinter.Toplevel(self)
        self.splash_window.overrideredirect(True)
        # open image file
        splash_file = Image.open('splash.png')
        # create ImageTk instance
        self.splash_photo_image = ImageTk.PhotoImage(splash_file)
        # assign ImateTk instance to label, and pack it
        self.splash_label = tkinter.Label(self.splash_window,
                                          image=self.splash_photo_image)
        self.splash_label.pack()

        self.progress = ttk.Progressbar(self.splash_window, orient="horizontal",
                                        length=self.splash_photo_image.width(),
                                        mode="determinate")
        self.progress.pack(side="bottom")

        self.bytes = 0
        self.maxbytes = 0
        self.finished = False
        self.start_splash()

    def start_splash(self):
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = self.maxbytes
        self.read_bytes()

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 500
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(10, self.read_bytes)
        else:
            self.splash_window.destroy()
            self.open_main_window()

    def open_main_window(self):
        self.geometry("256x256")
        self.main_label = tkinter.Label(self, text="This is main window.")
        self.main_label.pack()


app = App()
app.mainloop()