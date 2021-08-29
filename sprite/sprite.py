from sprite.si import sprite_si

class sprite:
    def __init__(self,canvas):
        self.canvas=canvas
        self.ur=1
        self.items=[self.canvas.create_rectangle(30,30,80,80,fill='blue'),self.canvas.create_rectangle(45,-20,65,30)]
        self.canvas.bind('<Button-3>',self.button3)
        self.canvas.bind('<Motion>',self.mot)
        self.canvas.bind('<Button-1>',self.button1)
        self.eventxy=[0,0]
        self.si=sprite_si(self.canvas)

    def loop(self):
        self.xy=self.canvas.coords(self.items[0])#調整方向
        if self.ur==1:
            self.canvas.delete(self.items[1])
            self.x=(self.xy[0]+self.xy[2])//2
            self.items[1]=self.canvas.create_rectangle(self.x-10,self.xy[1]-30,self.x+10,self.xy[1],fill='blue')
        elif self.ur==2 :
            self.canvas.delete(self.items[1])
            self.y=(self.xy[1]+self.xy[3])//2
            self.items[1]=self.canvas.create_rectangle(self.xy[2],self.y-10,self.xy[2]+30,self.y+10,fill='blue')
        elif self.ur==3:
            self.canvas.delete(self.items[1])
            self.x=(self.xy[0]+self.xy[2])//2
            self.items[1]=self.canvas.create_rectangle(self.x-10,self.xy[3],self.x+10,self.xy[3]+30,fill='blue')
        else: 
            self.canvas.delete(self.items[1])
            self.y=(self.xy[1]+self.xy[3])//2
            self.items[1]=self.canvas.create_rectangle(self.xy[0]-30,self.y-10,self.xy[0],self.y+10,fill='blue')

        self.x=self.eventxy[0]-(self.xy[0]+self.xy[2])//2
        self.y=self.eventxy[1]-(self.xy[1]+self.xy[3])//2
        self.canvas.move(self.items[0],self.x,self.y)

        self.si.loop(2)    

    def button3(self,event):
        self.ur+=1
        if self.ur>4:
            self.ur=1

    def mot(self,event):
        self.eventxy=[event.x,event.y]

    def button1(self,event):
        self.xy=self.canvas.coords(self.items[1])
        if self.ur==1:
            self.x=(self.xy[0]+self.xy[2])//2
            self.si.si([self.x-5,self.xy[1]-20,self.x+5,self.xy[1]],self.ur)
        elif self.ur==2:
            self.y=(self.xy[1]+self.xy[3])//2
            self.si.si([self.xy[2],self.y-5,self.xy[2]+50,self.y+5],self.ur)
        elif self.ur==3:
            self.x=(self.xy[0]+self.xy[2])//2
            self.si.si([self.x-5,self.xy[3],self.x+5,self.xy[3]+20],self.ur)
        else:
            self.y=(self.xy[1]+self.xy[3])//2
            self.si.si([self.xy[0]-50,self.y-5,self.xy[0],self.y+5],self.ur)