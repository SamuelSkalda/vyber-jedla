import tkinter
canvas = tkinter.Canvas(width=500, height=300, bg='white')
canvas.pack()

subor = open('vyber_jedal.txt', 'w')
jedlo = ('z','c','m','o')

def vykreslenie():
    farba = ('green','red','blue','orange')
    x = 10
    y = 100
    for i in range(4):
        canvas.create_rectangle(x,y,x+120,y+120,fill=farba[i])
        x += 121
    canvas.create_text(250,40,text='VÝBER JEDLA', font='Arial 30 bold',fill='red')
vykreslenie()

def klik(event):
    subor = open('vyber_jedal.txt', 'a')
    x1, y1, x2, y2 = event.x, event.y, event.x, event.y
    cj = canvas.find_overlapping(x1, y1, x2, y2)
    cj = cj[0]
    kod = entry1.get()
    if kod != '':
        riadok = kod+' '+jedlo[cj-1]
        subor.write(riadok+'\n')
    subor.close()
    
label1 = tkinter.Label(text='Kód študenta')
label1.pack()
entry1 = tkinter.Entry()
entry1.pack()
canvas.bind('<Button-1>',klik)