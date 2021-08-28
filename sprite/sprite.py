class sprite:
    def __init__(self,canvas):
        self.canvas=canvas
        self.ur=1
        self.items=[self.canvas.create_rectangle(30,30,80,80,fill='blue'),self.canvas.create_rectangle(45,-20,65,30)]
        self.canvas.bind('<Button-3>',self.button3)
        self.canvas.bind('<Motion>',self.mot)
        self.eventxy=[0,0]

    def loop(self):
        self.xy=self.canvas.coords(self.items[0])
        if self.ur==1:
            self.canvas.delete(self.items[1])
            self.x=(self.xy[0]+self.xy[2])//2
            self.canvas.create_rectangle(self.x-10,self.xy[1]-50,self.x+10,self.xy[1],fill='blue')
        elif self.ur==2 :
            pass
        elif self.ur==3:
            pass
        else: 
            pass

    def button3(self,event):
        self.ur+=1
        if self.ur>4:
            self.ur=1

    def mot(self,event):
        self.eventxy=[event.x,event.y]