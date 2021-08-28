from tkinter import*

class canvas(Canvas):
    def __init__(self):
        self.root=Tk()
        self.root.title('Shoot-the-enemy2')
        super(canvas,self).__init__(self.root,width=640,height=480,bg='#ffffff')
        self.pack()
        self.root.mainloop()