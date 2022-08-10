def abstand(s, t, dateiname = "labyrinth.dat"):
# Ist s = t, dann ist der abstand = 0 und wir sind fertig
    if s == t:
        return 0
        
# Die Zeilen von der Labyinth werden in eine Liste gefuegt
    reader = open(dateiname, "r")
    L1 = []
    for line in reader:
        L1.append(line)
    reader.close()

# Aus die jeweiligen Zeilen wird eine Liste mit Koordinaten a,b gemacht
    for i in range(0,len(L1)):
        L1[i] = list(L1[i])

# Alle P Knoten in eine Liste
    g = []
    for i in range(0, len(L1)):
        for j in range(0,len(L1[i])):
            if L1[i][j] == "P":
                a = (i,j)
                g.append(a)
# Nun alle Knoten \ s bzw. U
    g.remove(s)  

# Breitensuche faengt in s an :
    y = [s] # FIFO Schlange(First In First Out Queue)
    j = [] # List von neue erreichbare Knoten pro Iteration
    k = 0 # Anzahl von Iterationen
    for c in range(0,len(g)):
        while len(y) > 0: # Rechts, Links, Oben & Unten
            x = y[0]
            r = (x[0] + 1,x[1])
            l = (x[0] - 1,x[1])
            u = (x[0],x[1] - 1)
            d = (x[0],x[1] + 1)

    # If eine neue erreichbare Knote gefunden wird, wird es von der Liste(von gesuchte Knoten) entfernt 
    # Die Knote kommt dann aus eine Liste von neue Knoten
            if r in g:
                j.append(r)
                g.remove(r)
            if l in g:
                j.append(l)
                g.remove(l)
            if u in g:
                j.append(u)
                g.remove(u)
            if d in g:
                j.append(d)
                g.remove(d)
    # Suche fuer das 1. Knote in unsere Queue beendet
            y.pop(0)
    # Iteration vorbei
        k += 1

    #Ist t erreicht, dann Anzahl Iterationen = k und fertig
        for i in range(0,len(j)):
            if j[i] == t:
                return k
    # Es existiert keine neue Knote = t nicht erreichbar
        if len(j) == 0:
            return(-1)
    # Neue Knote, aber t nicht ereicht = neue Iteration, neue Knoten in Queue        
        y = j
        j = []