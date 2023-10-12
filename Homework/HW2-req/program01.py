# -*- coding: utf-8 -*-

"""
Consideriamo la codifica dei numeri romani e la modifica suggerita da 
Randall Munroe nel suo blog XKCD.
Nella codifica dei numeri romani:
- non esiste lo zero
- si usano le lettere 'IVXLCDM' che corrispondono ai valori decimali
  'I' = 1, 'V' = 5, 'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1000
- i numeri si scrivono da sinistra a destra cominciando con i valori più alti 
  (migliaia, centinaia, decine, unità)
- i valori delle lettere si sommano, tranne quando sono seguiti da lettere di peso maggiore, 
  nel qual caso si sottraggono
- si possono usare al massimo 3 lettere consecutive uguali per le lettere 'IXCM'
  ('III' = 3, 'XXX' = 30, 'CCC' = 300 , 'MMM' = 3000)
- per rappresentare i valori che hanno cifra decimale 4 o 9 si usa la sottrazione 
  dalla lettera seguente
  Es. 4 = 'IV'   9 = 'IX',    40 = 'XL'    39 = 'IXL'   499 = 'ID'

Nel suo blog XKCD, invece, Randall Munroe codifica i numeri romani con i corrispondenti numeri arabi: 
si concatenano i numeri arabi ottenuti sostituendo a ciascuna lettera il valore corrispondente.  
Es.    397 =>  'CCCXCVII' => 100 100 100 10 100 5 1 1 => '10010010010100511'
Chiamiamo questa codifica "formato XKCD".

Obiettivo dello homework è decodificare una lista di stringhe che rappresentano
numeri romani nel formato XKCD, e tornare i K valori maggiori in ordine decrescente.

Implementate quindi le seguenti funzioni:
"""

def decode_XKCD_tuple(xkcd_values : tuple[str, ...], k : int) -> list[int]:
    '''
    Riceve una lista di stringhe che rappresentano numeri nel formato XKCD
    ed un intero k positivo.
    Decodifica i numeri forniti e ne ritorna i k maggiori.

    Parameters
    valori_xkcd : list[str]     lista di stringhe in formato XKCD
    k : int                     numero di valori da tornare
    Returns
    list[int]                   i k massimi valori ottenuti in ordine decrescente
    '''
    # INSERISCI QUI IL TUO CODICE
    ris : list[int] =[]
    for xkcd in xkcd_values:
        pesi : list[int] = []
        i = 0
        s = False
        for x in range(len(xkcd)+1):
            j=x-1
            if(s):
                if(x<len(xkcd)):
                    if(xkcd[x]!="0"):
                        pesi.append(int(xkcd[i:x]))
                        i=x
                else:
                    if(xkcd[j]!="0"):
                        pesi.append(int(xkcd[j]))
                    else:
                        pesi.append(int(xkcd[i:j+1]))
            else:
                s = True
        n=0
        f=0
        for i in range(len(pesi)):
            if((i+1)<=len(pesi)-1):
                if(pesi[i]>=pesi[i+1]):    
                    n=n+pesi[i]
                else:
                    f=f+pesi[i]
            else:
                n=n+pesi[i]
        n=n-f
        ris.append(n)
    ris.sort()
    ris.reverse()
    return(ris[:k])
    pass


def decode_value(xkcd : str ) -> int:
    '''
    Decodifica un valore nel formato XKCD e torna l'intero corrispondente.

    Parameters
    xkcd : str                  stringa nel formato XKCD
    Returns
    int                         intero corrispondente
    
    Esempio: '10010010010100511' -> 397
    '''
    # INSERISCI QUI IL TUO CODICE
    pesi : list[int] = []
    l = False
    i=0
    for x in range(len(xkcd)+1):
        j=x-1
        if(l):
            if(x<len(xkcd)):
                if(xkcd[x]!="0"):
                    pesi.append(int(xkcd[i:x]))
                    i=x
            else:
                if(xkcd[j]!="0"):
                    pesi.append(int(xkcd[j]))
                else:
                    pesi.append(int(xkcd[i:j+1]))
        else:
            l = True
    n=0
    s=0
    for i in range(len(pesi)):
        if((i+1)<=len(pesi)-1):
            if(pesi[i]>=pesi[i+1]):    
                n=n+pesi[i]
            else:
                s=s+pesi[i]
        else:
            n=n+pesi[i]
    n=n-s
    return(n)
    pass


def xkcd_to_list_of_weights(xkcd : str) -> list[int]:
    '''
    Spezza una stringa in codifica XKCD nella corrispondente
    lista di interi, ciascuno corrispondente al peso di una lettera romana

    Parameters
    xkcd : str              stringa nel formato XKCD
    Returns
    list[int]               lista di 'pesi' corrispondenti alle lettere romane

    Esempio: '10010010010100511' -> [100, 100, 100, 10, 100, 5, 1, 1,]
    '''
    # INSERISCI QUI IL TUO CODICE
    pesi : list[int] = []
    i = 0
    #l è una variabile booleana che serve ad "accendere" il resto del programma dopo la prima iterazione
    l = False
    for x in range(len(xkcd)+1):
        if(l):
            if(x<len(xkcd)):
                if(xkcd[x]!="0"):
                    pesi.append(int(xkcd[i:x]))
                    i=x
            else:
                if(xkcd[x-1]!="0"):
                    pesi.append(int(xkcd[x-1]))
                else:
                    pesi.append(int(xkcd[i:x]))
        else:
            l = True
    return(pesi)
    pass


def list_of_weights_to_number(weigths : list[int] ) -> int:
    '''
    Trasforma una lista di 'pesi' nel corrispondente valore arabo
    tenendo conto della regola di sottrazione

    Parameters
    lista_valori : list[int]    lista di 'pesi' di lettere romane
    Returns
    int                         numero arabo risultante
    
    Esempio: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397
    '''
    # INSERISCI QUI IL TUO CODICE
    pesi=weigths
    n=0
    s=0
    for i in range(len(pesi)):
        if((i+1)<=len(pesi)-1):
            if(pesi[i]>=pesi[i+1]):    
                n=n+pesi[i]
            else:
                s=s+pesi[i]
        else:
            n=n+pesi[i]
    n=n-s
    return(n)
    pass



###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('10010010010100511', decode_value('10010010010100511'), '(397?)')

