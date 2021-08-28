class sprite_si:
    def __init__(self,canvas):
        self.canvas=canvas
        self.items=[]
    def si(self,xy,ur):
        self.items.append([self.canvas.create_rectangle(xy[0],xy[1],xy[2],xy[3]),ur])
    def loop(self,tu):
        self.xys=[]
        for item in range(len(self.items)):
            if item<len(self.items):

                if self.items[item][1]==1:
                    self.canvas.move(self.items[item][0],0,-10)
                elif self.items[item][1]==2:
                    self.canvas.move(self.items[item][0],10,0)
                elif self.items[item][1]==3:
                    self.canvas.move(self.items[item][0],0,10)
                else:
                    self.canvas.move(self.items[item][0],-10,0)
                self.xys.append(self.canvas.coords(self.items[item][0]))

                self.xy=self.canvas.coords(self.items[item][0])
                if self.xy[0]<0 or self.xy[1]<0 or self.xy[2]>640 or self.xy[3]>480: #or tu[item]==1:
                    self.canvas.delete(self.items[item][0])
                    del self.items[item]
