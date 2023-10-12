#Funzione per la lettura del file
def TextReader(nome:str)->list[str]:

    #lista da ritornare
    prin : list[str] = []

    #oggetto file per la raccolta delle righe e raccolta in questione
    filez=open(nome, "r", encoding="utf-8")
    prin=filez.read().replace("\t","\n").replace(" ","\n").split("\n")
    filez.close()

    prin=[i for i in prin if i != ""]
        
    return(prin)

def group(start:str)->list[str]:

    #dichiarazoine degli elementi in uso nel ciclo seguente
    parole : list[str] = []
    supp : list[str]=TextReader(start)

    #ciclo per la lettura e la raccolta di tutte le parole dei file nella lista parole
    while(True):

        for i in supp[1:]:
            parole.append(i)   

        if(supp[0]==start):
            break

        #raccolta della prossima lista
        supp=TextReader(str(supp[0]))
    return(parole)

def count(parole:list[str])->dict[bytes:int]:

    #ciclo da fare per il conteggio delle lettere nelle loro posizioni
    i=0
    diz : list[dict[bytes:int]] = []
    
    for i in range(len(max(parole, key=len))):
        s=False
        grafo : dict = {}
        j=0

        for j in range(len(parole)): 

            if (i<=len(parole[j])-1) and (parole[j][i]!=[]):
                grafo[parole[j][i]]=grafo.get(parole[j][i],0)+1
                s=True

        if(s):
            diz.append(grafo)
    return(diz)

def MakeString(diz:list[dict[bytes:int]])->str:

    #ciclo per l'output della lettera con più frequenza in una determinata posizione
    i=0
    g : str = ""

    for i in range(len(diz)):

        #valore massimo nel dizionario 
        m=max(diz[i].values())
        #conteggio delle volte che compare m nel dizionario
        y=list(diz[i].values()).count(m)
        f=0
        supp=[]
        for x in diz[i]:
            
            if(f>=y): break
            
            if(diz[i].get(x)==m):
                supp.append(x)
                f+=1
            
        
        g=g+min(supp)

    return(g)

#MAIN
start : str="test03/woodchuck.txt"

print(MakeString(count(group(start))))