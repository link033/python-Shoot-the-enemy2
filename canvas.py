from tkinter import*
from sprite.sprite import sprite
import time

class canvas(Canvas):
    def __init__(self):
        self.root=Tk()
        self.root.title('Shoot-the-enemy2')
        super(canvas,self).__init__(self.root,width=640,height=480,bg='#ffffff')
        self.pack()
        self.setp()
        while True :
            self.loop()
            self.root.update()
            time.sleep(0.01)
        self.root.mainloop()
    
    def setp(self):
        self.sprite=sprite(self)

    def loop(self):
        self.sprite.loop()