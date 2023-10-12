#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Siete stati appena ingaggiati in una software house di videogiochi e
dovete renderizzare su immagine il giochino dello snake salvando
l'immagine finale del percorso dello snake e restituendo la lunghezza
dello snake.
Si implementi la funzione generate_snake che prende in ingresso un
percorso di un file immagine, che e' l'immagine di partenza
"start_img" che puo' contenere pixel di background neri, pixel di
ostacolo per lo snake di colore rosso e infine del cibo di colore
arancione. Lo snake deve essere disegnato di verde. Inoltre bisogna
disegnare in grigio la scia che lo snake lascia sul proprio
cammino. La funzione inoltre prende in ingresso una posizione iniziale
dello snake, "position" come una lista di due interi X e Y. I comandi
del giocatore su come muovere lo snake nel videogioco sono disponibili
in una stringa "commands".  La funzione deve salvare l'immagine finale
del cammino dello snake al percorso "out_img", che e' passato come
ultimo argomento di ingresso alla funzione. Inoltre la funzione deve
restituire la lunghezza dello snake al termine del gioco.

Ciascun comando in "commands" corrisponde ad un segno cardinale ed e
seguito da uno spazio. I segni cardinali possibli sono:

| NW | N | NE |
| W  |   | E  |
| SW | S | SE |

che corrispondono a movimenti dello snake di un pixel come:

| alto-sinistra  | alto  | alto-destra  |
| sinistra       |       | destra       |
| basso-sinistra | basso | basso-destra |

Lo snake si muove in base ai comandi passati e nel caso in cui
mangia del cibo si allunga di un pixel.

Lo snake puo' passare da parte a parte dell'immagine sia in
orizzontale che in verticale. Il gioco termina quando sono finiti i
comandi oppure lo snake muore. Lo snake muore quando:
- colpisce un ostacolo
- colpisce se stesso quindi non puo' passare sopra se stesso
- si incrocia in diagonale in qualsiasi modo. Ad esempio, un percorso
  1->2->3-4 come quello sotto a sinistra non e' lecito mentre quello a
  destra sotto va bene.

  NOT OK - diagonal cross        OK - not a diagonal cross
       | 4 | 2 |                    | 1 | 2 |
       | 1 | 3 |                    | 4 | 3 |

Ad esempio considerando il caso di test data/input_00.json
lo snake parte da "position": [12, 13] e riceve i comandi
 "commands": "S W S W W W S W W N N W N N N N N W N" 
genera l'immagine in visibile in data/expected_end_00.png
e restituisce 5 in quanto lo snake e' lungo 5 pixels alla
fine del gioco.

NOTA: analizzate le immagini per avere i valori esatti dei colore da usare.

NOTA: non importate o usate altre librerie
'''

import images

#funzione di controllo di fine lista e applicazione dell'effetto pacman
def pacEffect(z:int,Zmax:int)->int:

    #Controlli sul limite della tabella e sul valore attuale
    if z>Zmax: z = 0
    elif z<0: z = Zmax

    return z

#controllo di fine per incroci diagonali
def diag(pre:list, x:int, y:int, Xmax:int, Ymax:int)->bool:

    #x e y sono le coordinate della posizione futura, quella in analisi

    #ultima posizione registrata 
    c=pre[len(pre)-1]
    
    #definizione dell'intorno e delle zone che sono occupate
    intorno:list=[(c[0]-1,c[1]+1),(c[0]-1,c[1]-1),(c[0]-1,c[1]),(c[0]+1,c[1]-1),(c[0]+1,c[1]),(c[0]+1,c[1]+1),(c[0],c[1]-1),(c[0],c[1]+1)]
    occupato:list=[f for f in pre if f in intorno]
    
    #variabili per il controllo dei pixel intorno alla posizione di arrivo
    #rispettivamente indicano: x1=W x2=E y1=S y2=N
    x1=pacEffect(x+1, Xmax)
    x2=pacEffect(x-1, Xmax)
    y1=pacEffect(y+1, Ymax)
    y2=pacEffect(y-1, Ymax)

    #casi che indicano se passa in una direzione diagonale non valida
    SW:bool=(((x1,y) in occupato) and ((x,y1) in occupato))
    NW:bool=(((x1,y) in occupato) and ((x,y2) in occupato))
    SE:bool=(((x2,y) in occupato) and ((x,y1) in occupato))
    NE:bool=(((x2,y) in occupato) and ((x,y2) in occupato))

    #variabile che determina la presenza o meno di un incrocio diagonale
    s=(SW or NW or SE or NE)
    
    return s

#funzione di movimento del serpente con coordinate
def move(i:str, x:int, y:int, Xmax:int, Ymax:int)->tuple[int,int]:

    #Controllo di movimento NSWE e varianti diagonali
    if i.startswith("N"):
        y=y-1
        if i=="NW":
            x=x-1
            
        elif i=="NE":
            x=x+1
                                   
    elif i.startswith("S"):
        y=y+1
        if i=="SW":
            x=x-1

        elif i=="SE":
            x=x+1

    elif i=="W":
        x=x-1
    else:
        x=x+1
    
    #controllo effetto pac-man
    x=pacEffect(x, Xmax)
    y=pacEffect(y, Ymax)

    return x,y

#funzione per la colorazione del serpente con controlli di fine
def color(com:list, pos:list[int,int], img:list)->int:
    #definizione delle coordinate di partenza e dei limiti dell'immagine
    x:int=pos[0]
    y:int=pos[1]
    Ymax:int=len(img)-1
    Xmax:int=len(img[y])-1

    #definizione della lista contenente le n posizioni precedenti del serpente
    pre:list[tuple(int,int)]=[(x,y)]

    #variabile di switch che modula la lunghezza di pre
    n:bool=True

    #dizionario che fa da color map per il programma
    CMap : dict = {"red":(255,0,0), "green":(0,255,0), "orange":(255,128,0), "grey":(128,128,128), "black":(0,0,0)}

    #colorazione della casella di partenza
    img[y][x]=CMap["grey"]

    #ciclo per l'interpretazione dei comandi e del percorso del serpente
    for i in com:

        #raccolta delle istruzioni dopo l'esecuzione del comando
        x,y=move(i, x, y, Xmax, Ymax)

        #Controlli di colore
        if(img[y][x]!=CMap["black"]):
            #controllo di allungamento del serpente
            if(img[y][x]==CMap["orange"]):
                n=False
            #controllo primario di fine programma
            elif(img[y][x]==CMap["red"]):
                break
        #controllo secondario di fine programma
        if ((x,y) in pre) or (diag(pre, x, y, Xmax, Ymax)):
                break

        #inserimento dell'istruzione nella lista dei precedenti
        pre.append((x,y))
        #con pulizia della prima istruzione ormai passata
        if(n):pre.pop(0)
        else:n=True 

        #colorazione grigia dove passa il serpente
        img[y][x]=CMap["grey"]
    #ciclo di colorazione verde del serpente tramite le sue ultime posizioni
    for j in pre:
        img[j[1]][j[0]]=CMap["green"]

    return len(pre)

#funzione di inizio e fine del programma        
def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    # Scrivi qui il tuo codice
    #tabella(lista*lista) di pixel(tuple rgb) e lista dei comandi
    img:list = images.load(start_img)
    com:list = commands.split(" ")
    
    #risultato e inizio della modifica dell'immagine
    l:int=color(com, position, img)

    #salvataggio dell'immagine e conclusione del programma
    images.save(img,out_img)
    return l
    pass