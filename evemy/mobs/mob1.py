import random

class mob1:
    def __init__(self,canvas):
        self.canvas=canvas
        self.items=[]
    def ud(self):
        self.random=random.randint(1,2)
        if self.random==1:
            self.random=random.randint(1,2)
            if self.random==1:
                self.random=random.randint(0,590)
                self.items.append([self.canvas.create_rectangle(self.random,-50,self.random+50,0),0])