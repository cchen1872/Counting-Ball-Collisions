def find_zeroes(a,b,c):
    v1 = ((b**2 - 4*a*c)**0.5 - b)/2/a
    return(v1)
def one():
    canvas.delete('all')
    m[0] = 1
    run()

def hundred():
    canvas.delete('all')
    m[0] = 100
    run()
    
def ten_thousand():
    canvas.delete('all')
    m[0] = 10000
    run()

def run():
    canvas.create_line(10,0,10,270,fill = 'white')
    canvas.create_line(10,270,450,270,fill = 'white')
    for i in range(0,10):
        canvas.create_line(10,10 + 27*i,0,25 + 27*i,fill = 'white')
    m1 = canvas.create_rectangle(100,240,130,270,fill = 'blue')
    m2 = canvas.create_rectangle(250,220,300,270,fill = 'lightgrey')
    m1_t = canvas.create_text(115,255,text = '1 kg',fill = 'white')
    m2_t = canvas.create_text(275,255,text = ('10^'+ str(int(math.log10(m[0]))) + ' kg'),fill = 'black')
    v = [0,-0.05];
    k = [m[0] * v[1]** 2,m[0] * v[1]]

    counter[0] = 0
    counter_text[0] = canvas.create_text(200,100,text = counter[0],fill = 'white', font = ('Comic Sans MS',40))
    print(m[0])
    stop_updating= [False]
    def update_movement():
        if canvas.coords(m1)[2] >= canvas.coords(m2)[0]:
            continues[0] = 1
            continues[1] = 0
        if canvas.coords(m1)[0] + v[0] <= 10 and continues[1] == 0:
            continues[0] = 2
        if continues[0] == 1:
            v[1] = find_zeroes((m[0]**2)+(m[0]),-2*k[1]*m[0],(k[1]**2)-k[0])
            v[0] = k[1] - (m[0] * v[1])
            counter[0] += 1
            continues[0] = 0
            canvas.delete(counter_text[0])
            counter_text[0] = canvas.create_text(200,100,text = counter[0],fill = 'white', font = ('Comic Sans MS',40))
            print(v)
        if continues[0] == 2 and continues[1] == 0:
            print(canvas.coords(m1)[0] - 10,((canvas.coords(m1)[0] - 10) * v[1] / v[0]))
            #canvas.move(m1,canvas.coords(m1)[0] - 10,0)
            #canvas.move(m1_t,canvas.coords(m1)[0] - 10,0)
            #canvas.move(m2,((canvas.coords(m1)[0] - 10) * v[1] / v[0]),0)
            #canvas.move(m2_t,((canvas.coords(m1)[0] - 10) * v[1] / v[0]),0)
            v[0] = -v[0]
            k[1] = v[0] + m[0]*v[1]
            continues[1] = 1
            continues[0] = 0
            counter[0] += 1
            canvas.delete(counter_text[0])
            counter_text[0] = canvas.create_text(200,100,text = counter[0],fill = 'white', font = ('Comic Sans MS',40))
        else:
            canvas.move(m2,v[1],0)
            canvas.move(m2_t,v[1],0)
            canvas.move(m1,v[0],0)
            canvas.move(m1_t,v[0],0)        
        if not stop_updating[0]:
            root.after(1,update_movement)
    root.after(0,update_movement)
from tkinter import *
import math
root = Tk()
root.wm_title('Pi Phenomenon')
root.geometry('450x300')
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="1 kg", command=one)
filemenu.add_command(label="100 kg", command=hundred)
filemenu.add_command(label="10000 kg", command=ten_thousand)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu = menubar)
canvas = Canvas(master = root,height = 620,width = 450,bg= 'black')
canvas.pack()
#c = canvas.create_oval(75,300,375,600,fill = 'aliceblue')
stop_updating= [False]
continues = [0,0]
m = [100]
counter = [0]
counter_text = [0]
run()
root.mainloop()
