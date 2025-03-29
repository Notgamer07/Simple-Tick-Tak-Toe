from tkinter import Button, Tk, DISABLED, NORMAL, RAISED

class gui:
    def __init__(self,root):
        self.root = root
        self.setup()
        self.o=[]
        self.x=[]
        self.winning_condition=[[0,1,2],#horizontal
                                [3,4,5],#horizontal
                                [6,7,8],#horizontal
                                [0,4,8],#diagonal
                                [2,4,6],#diagonal
                                [0,3,6],#Vertical
                                [1,4,7],#Vertical
                                [2,5,8]]#Vertical
        self.set_state = 0
        self.isdisabled = False
        self.setup()
    
    def setup(self):
        self.options=[]
        for i in range(3):
            for j in range(3):
                btn = Button(self.root, padx=25, pady=20, text="  ",font=("Arial", 12, "bold"),bd=4)
                btn.grid(row=i,column=j)
                btn.config(command=lambda btn=btn: self.pressed(btn))
                self.options.append(btn)
        self.retry_button=Button(self.root,command=self.retry,text="RETRY",font=("Arial", 12, "bold"),fg='yellow',bg='gray',relief=RAISED).grid(row=3,column=1)

    def pressed(self, btn):
        index = self.options.index(btn)
        if index in self.o:
            pass
        elif index in self.x:
            pass
        elif self.set_state == 0:
            btn.config(text="O")
            self.set_state = 1
            self.o.append(index)
        else:
            btn.config(text='X')
            self.set_state = 0
            index = self.options.index(btn)
            self.x.append(index)
        self.check()

    def check(self):
        if(sorted(self.o) in self.winning_condition):
            for i in sorted(self.o):
                self.options[i].config(bg='green',disabledforeground='white')
                self.disable_btn()
        if(sorted(self.x) in self.winning_condition):
            for i in sorted(self.x):
                self.options[i].config(bg='green',disabledforeground='white')
                self.disable_btn()
        
    def disable_btn(self):
        self.isdisabled = True
        for i in self.options:
            i.config(state=DISABLED)
    
    def retry(self):
        self.o = []
        self.x = []
        self.set_state = 0
        if (self.isdisabled):
            self.isdisabled = False
        self.normal_btn()
        
    
    def normal_btn(self):
        for i in self.options:
            i.config(state=NORMAL,text="  ",fg='black',bg='white')


root =Tk()
app=gui(root)
root.mainloop()