import tkinter
canvas = tkinter.Canvas(width=500, height=300, bg='white')
canvas.pack() #upravenie platna

subor = open('vyber_jedal.txt', 'w') #otvorenie suboru na pisanie
jedlo = ('z','c','m','o') #n-tica "jedal"

def vykreslenie(): #funkcia na vykreslenie
    farba = ('green','red','blue','orange') #n-tica farieb 
    x = 10 #nastavenie x na 10
    y = 100 #nastavenie y na 100
    for i in range(4): #frcyklus na vykreslenie stvorcekov
        canvas.create_rectangle(x,y,x+120,y+120,fill=farba[i]) #prikaz na vykreslenie stvorceka
        x += 121 #pripocitanie ku x aby sa stvorceky nevykreslili cez seba
    canvas.create_text(250,40,text='VÝBER JEDLA', font='Arial 30 bold',fill='red') #vypisanie nadpisu
vykreslenie() #zavolanie funkcie vykreslenie

def klik(event): #funkcia na vykonanie po kliknuti
    subor = open('vyber_jedal.txt', 'a') #otvorenie suboru na upravu
    x1, y1, x2, y2 = event.x, event.y, event.x, event.y #nastavenie premennych podla miesta kliknutia
    cj = canvas.find_overlapping(x1, y1, x2, y2) #prikaz na vratenie n-tice s cislom na ktory stvorcek som klikol
    cj = cj[0] #upravenie do premennej lebo do n-tice vracia aj ciarku tak aby z nej bralo len nultu hodnotu
    kod = entry1.get() #zadanie kodu pouzivatelom do premennej kod
    if kod != '': #podmienka ak kod nie je prazdny
        riadok = kod+' '+jedlo[cj-1] #zapisanie kodu a vyberu jedla do riadku
        subor.write(riadok+'\n') #zapisanie riadku do suboru
    subor.close() #uzatvorenie suboru
    
label1 = tkinter.Label(text='Kód študenta') #vytvorenie napisu nad miestom zadania kodu uzivatelom
label1.pack()
entry1 = tkinter.Entry() #vytvorenie vstupneho pola
entry1.pack()
canvas.bind('<Button-1>',klik) #bindovanie laveho tlacitka mysi po kliknuti sa zavola funkcia klik
