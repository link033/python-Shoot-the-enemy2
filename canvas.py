from tkinter import*
from sprite.sprite import sprite
from evemy.mobs.mob1 import mob1
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
        self.mob1=mob1(self)
        self.dk=0

    def loop(self):
        self.sprite.loop()
        self.dk+=1
        if self.dk>100:
            self.dk=0
            self.mob1.ud()
        self.mob1.loop()