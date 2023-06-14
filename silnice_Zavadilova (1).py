import tkinter

p = tkinter.Canvas(width=1000, height=500, bg="green")
p.grid(columnspan=3, row=0)

jede = True
stisk = False
vagon = False
light = "green"
pozice = 0
pozice_auto = 0
pozice_autobus = 0
jede_autobus=True
jede_auto=True

def start():
    global stisk
    if stisk==False:
        autobus()
        auto()
        vlak()
        stisk=True
def pohyb():
    global jede
    if jede:
        jede=False
    else:
        jede=True
        auto()
        autobus()
        vlak()

label_1=tkinter.Label(text="Počet vagónů:")
label_1.grid(column=0, row=1)

enter_1=tkinter.Entry(width="4")
enter_1.grid(column=1, row=1, sticky="w")
enter_1.insert(1, "1")

button_1=tkinter.Button(text="Start", command=start, width="15")
button_1.grid(column=1, row=1, sticky="e")

button_2=tkinter.Button(text="Zastav/pokračuj", command=pohyb, width="15")
button_2.grid(column=2, row=1, sticky="w")

p.create_rectangle(450, 0, 550, 500, fill="grey", outline="")
p.create_rectangle(0, 200, 1000, 300, fill="grey", outline="grey")

shift_v=0
shift_h=0

for i in range(17):
    p.create_rectangle(495, 0+shift_v, 505, 15+shift_v, fill="white")
    shift_v += 30
for i in range(34):
    p.create_rectangle(0+shift_h, 245, 15+shift_h, 255, fill="white")
    shift_h += 30

yc=0
yb=0

def auto():
    global jede
    global jede_auto
    global pozice_auto
    if 200 > pozice_auto> 185 and 450-length < pozice < 490:
        jede_auto = False
        p.after(10, auto)
    elif pozice >= 540 or pozice <= 500-length:
        jede_auto = True
    if jede and jede_auto:
        global yc
        p.delete("auto")
        p.create_rectangle(465, 0+yc, 485, 40+yc, tag="auto", outline="", fill="red")
        yc += 4
        if yc == 500:
            yc = 0
        pozice_auto = 40 + yc
        p.after(10, auto)

def autobus():
    global jede
    global jede_autobus
    global pozice_autobus
    if 260 > pozice_autobus> 240 and 500-length < pozice < 540:
        jede_autobus = False
        p.after(10, autobus)
    elif pozice >= 540 or pozice <= 500-length:
        jede_autobus = True
    if jede and jede_autobus:
        global yb
        p.delete("autobus")
        p.create_rectangle(515, 500-yb, 535, 460-yb, tag="autobus", outline="",fill="green")
        yb += 5
        if yb == 500:
            yb = 0
        pozice_autobus = 460 - yb
        p.after(10, autobus)

p.create_rectangle(560, 150, 670, 190, fill="black")
p.create_oval(565, 155, 595, 185)
p.create_oval(600, 155, 630, 185,outline="", fill="#BB6700")
p.create_oval(635, 155, 665, 185)

def provoz_stisk(i):
    provoz()

def provoz():
    global light
    if light == "green":
        p.create_oval(565, 155, 595, 185, outline="", fill="dark red")
        p.create_oval(635, 155, 665, 185, outline="",fill="green")
        light="red"
        if stisk:
            vlak()
    else:
        p.create_oval(565, 155, 595, 185, outline="", fill="red")
        p.create_oval(635, 155, 665, 185, outline="", fill="dark green")
        light="green"
yt = 0
vlak_move=0
length = 0

def vlak():
    if jede==True and light=="red":
        global vlak_move
        global vagon
        global pozice
        global length
        yr = 0
        enter_1_shift = 1000 + (int(enter_1.get())*44)
        number = vlak_move*4
        length = 44*int(enter_1.get())
        
        if vagon == False:
            for i in range(int(enter_1.get())):
                p.create_rectangle(956-yr, 210, 996-yr, 230, tag="vlak", outline="", fill="yellow")
                p.create_oval(961-yr, 225, 971-yr, 235, tag="vlak", outline="",fill="black")
                p.create_oval(981-yr, 225, 991-yr, 235, tag="vlak", outline="",fill="black")
                yr += 44
                vagon = True
            pozice = (1000 - number) - length
        if number%enter_1_shift == 0 and number/enter_1_shift != 1 and number/enter_1_shift != 0:
            for i in range(int(enter_1.get())):
                p.create_rectangle(1000-yr, 210, 1040-yr, 230, tag="vlak",outline="", fill="yellow")
                p.create_oval(1005-yr, 225, 1015-yr, 235, tag="vlak", outline="",fill="black")
                p.create_oval(1025-yr, 225, 1035-yr, 235, tag="vlak", outline="",fill="black")
                yr -= 44
            pozice = 1000 
        elif vlak_move==250:
            for i in range(int(enter_1.get())):
                p.create_rectangle(1000-yr, 210, 1040-yr, 230, outline="", tag="vlak", fill="yellow")
                p.create_oval(1005-yr, 225, 1015-yr, 235, outline="",tag="vlak", fill="black")
                p.create_oval(1025-yr, 225, 1035-yr, 235, outline="", tag="vlak", fill="black")
                yr -= 44
            pozice = 1000
        p.move("vlak", -4, 0)
        vlak_move += 1
        pozice -= 4
        print(pozice)
        p.after(10, vlak)


provoz()
p.bind("<Button-1>", provoz_stisk)
p.mainloop()


