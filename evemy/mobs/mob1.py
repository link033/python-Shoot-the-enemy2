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
            else:
                self.random=random.randint(0,590)
                self.items.append([self.canvas.create_rectangle(self.random,480,self.random+50,530),0])
        else:
            self.random=random.randint(1,2)
            if self.random==1:
                self.random=random.randint(0,430)
                self.items.append([self.canvas.create_rectangle(-50,self.random,0,self.random+50),0])
            else:
                self.random=random.randint(0,590)
                self.items.append([self.canvas.create_rectangle(640,self.random,690,self.random+50),0])
 
    def loop(self):
        for item in range(len(self.items)):
            if item<len(self.items):
                self.xy=self.canvas.coords(self.items[item][0])
                if self.items[item][1]==0 and self.xy[0]<0:
                    self.canvas.move(self.items[item][0],10,0)
                elif self.items[item][1]==0 and self.xy[2]>640:
                    self.canvas.move(self.items[item][0],-10,0)
                elif self.items[item][1]==0 and self.xy[1]<0:
                    self.canvas.move(self.items[item][0],0,10)
                elif self.items[item][1]==0 and self.xy[3]>480:
                    self.canvas.move(self.items[item][0],0,-10)