#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Obiettivo dello homework è leggere alcune stringhe contenute in una serie di
file e generare una nuova stringa a partire da tutte le stringhe lette.
Le stringhe da leggere sono contenute in diversi file, collegati fra loro a
formare una catena chiusa. Infatti, la prima stringa di ogni file è il nome di
un altro file che appartiene alla catena: partendo da un qualsiasi file e
seguendo la catena, si ritorna sempre nel file di partenza.

Esempio: il contenuto di "A.txt" inizia con "B.txt", il file "B.txt", inizia
con "C.txt" e il file "C.txt" inizia con "A.txt", formando la catena
"A.txt"-"B.txt"-"C.txt".

Oltre alla stringa con il nome del file successivo, ogni file contiene anche
altre stringhe separate da spazi, tabulazioni o caratteri di a capo. La
funzione deve leggere tutte le stringhe presenti nei file della catena e
costruire la stringa che si ottiene concatenando i caratteri con la più alta
frequenza in ogni posizione. Ovvero, nella stringa da costruire, alla
posizione p ci sarà il carattere che ha frequenza massima nella posizione p di
ogni stringa letta dai file. Nel caso in cui ci fossero più caratteri con
la stessa frequenza, si consideri l'ordine alfabetico.
La stringa da costruire ha lunghezza pari alla
lunghezza massima delle stringhe lette dai file.

Quindi, si deve scrivere una funzione che prende in ingresso una stringa A 
che rappresenta il nome di un file e restituisce una stringa.
La funzione deve costruire la stringa secondo le indicazioni illustrate sopra
e ritornare le stringa così costruita.

Esempio: se il contenuto dei tre file A.txt, B.txt e C.txt nella directory
test01 è il seguente

test01/A.txt          test01/B.txt         test01/C.txt                                                                 
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite                                                                       
garden                park                 hello                                                                       
kitchen               affair               portrait                                                                     
balloon                                    angel                                                                                                                                               
                                           surfing                                                               

la funzione most_frequent_chars("test01/A.txt") dovrà restituire la stringa
"hareennt".
'''
###############################################################################

def cont(parole:list, i:int)->dict:
    grafo:dict={}
    
    for j in parole:
        
        if (i<=len(j)-1) and (j[i]!=[]):
            grafo[j[i]]=grafo.get(j[i],0)+1

    return(grafo)
    
###############################################################################

#Funzione per la lettura del file
def TReader(nome:str)->list[str]:
    
    #lista da ritornare
    prin : list[str] = []

    #oggetto file per la raccolta delle righe e raccolta in questione
    filez=open(nome, "r", encoding="utf-8")
    prin=filez.read().replace("\t","\n").replace(" ","\n").split("\n")
    filez.close()
    
    prin=[i for i in prin if i != ""]
        
    return(prin)

###############################################################################

def group(start:str)->list[str]:

    #dichiarazoine degli elementi in uso nel ciclo seguente
    parole : list[str] = []
    supp : list[str]=TReader(start)

    #ciclo per la raccolta di tutte le parole dei file nella lista parole
    while supp[0]!=start:
        
        parole.extend(supp[1:])

        #raccolta della prossima lista
        supp=TReader(supp[0])
    else:
        parole.extend(supp[1:])
    return(parole)

###############################################################################

def app(parole:list[str])->list[dict]:

    #ciclo da fare per il conteggio delle lettere nelle loro posizioni
    diz : list[dict] = []
    #l=len(parole)
    ll=len(max(parole, key=len))
    
    for i in range(ll):
        diz.append(cont(parole, i))
            
    return(diz)

###############################################################################

def most_frequent_chars(filename: str) -> str:
    # SCRIVI QUI LA TUA SOLUZIONE
    diz:list[dict]=app(group(filename))
    g : str = ""
    #ciclo per l'output della lettera con più frequenza in ogni posizione
    for i in diz:
        #valore massimo nel dizionario 
        m=max(i.values())
        #conteggio delle volte che compare m nel dizionario
        #y=list(i.values()).count(m)
        #f=0
        supp:list=[]
        for x in i:
            
            if(i[x]==m):
                supp.append(x)
                #f+=1
      
        g=g+min(supp)

    return(g)
    pass

###############################################################################