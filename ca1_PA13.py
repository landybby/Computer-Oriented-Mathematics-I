import copy
from collections import deque

    
#Teilkarten werden aus dem Inputfile generiert
def extractPartialMaps():
    inputfile = open('students.in', 'r')
    partialMap0, partialMap1, partialMap2, partialMap3 = ([] for i in range(4))
    cnt = 1
    for line in inputfile:
        if cnt % 8 != 0 and cnt < 8:
            partialMap0.append(list(line.rstrip('\n')))
        elif cnt % 8 != 0 and cnt < 16:
            partialMap1.append(list(line.rstrip('\n')))
        elif cnt % 8 != 0 and cnt < 24:
            partialMap2.append(list(line.rstrip('\n')))
        elif cnt % 8 != 0:
            partialMap3.append(list(line.rstrip('\n'))) 
        cnt += 1
    return [partialMap0, partialMap1, partialMap2, partialMap3]

# Knoten der Teilgraphen werden aus den Teilkarten extrahiert   
def verticesFromMaps(partialMaps):

    ### hier Funktion zur Ermittlung der Knoten
    k = 0 
    topleftVertices, toprightVertices, bottomleftVertices, bottomrightVertices = ([] for x in range(4))
     # = [(Index der Zeile, Index der Spalte)] 
    allVertices = [topleftVertices, toprightVertices, bottomleftVertices, bottomrightVertices]
    while k in range(4):
        for i in range(7):
            for j in range(10):
                if partialMaps[k][i][j] == "P" and (i == 0 or j == 0 or i == 6 or j == 9):
                    allVertices[k].append((i,j))
        k += 1
    for i in range (4):
        allVertices[i].sort()
    return allVertices

# Liste von Listen gewichteter Kanten der Teilgraphen
def edgesFromMaps(partialMaps,allVertices):
    topleftEdge, toprightEdge, bottomleftEdge, bottomrightEdge = ([] for x in range(4))
    allEdges = [topleftEdge, toprightEdge, bottomleftEdge, bottomrightEdge]
    i = 0
    j = 0
    while i in range(4):
        for j in range(len(allVertices[i])):
            for k in range(j+1,len(allVertices[i])):
                gewicht = distance(allVertices[i][j],allVertices[i][k],partialMaps[i])
                if 0 < gewicht:
                    allEdges[i].append([allVertices[i][j],allVertices[i][k],gewicht])
            j += 1
        i += 1
### bei den Kanten sollten die Vertices sortiert sein
### zB mittels: l = [knoten1,knoten2]
### l.sort *! wuerde das Liste nicht bei verticesFromMap schon sortiert?
### edge = [[l[0],l[1],gewicht]]    
    for i in range(4):
        allEdges[i].sort(key=takeThird, reverse=True)
        allEdges[i].sort(key=takeSecond)
        allEdges[i].sort(key=takeFirst)
    return allEdges

# Liste der Knoten des Top-Graphen
def generateTopVertices(partialMapVertices):
    topVertices = []
    for v in partialMapVertices[0]:
        topVertices.append(v)
    for v in partialMapVertices[3]:
        topVertices.append(vertexShiftUp(v,3))
    topVertices.sort()
    return topVertices

# Liste der gewichteten Kanten des Top-Graphen
def generateTopEdges(partialMapsEdges):
  sEdges = []
  tEdges = []
  topEdges = []
  i = 0
  while i in range(4):
    sEdges.append([])
    tEdges.append([])
    for k in range(len(partialMapsEdges[i])):
        sEdges[i].append(partialMapsEdges[i][k][0])
        tEdges[i].append(partialMapsEdges[i][k][1])
        topEdges.append([vertexShiftUp(sEdges[i][k],i),vertexShiftUp(tEdges[i][k],i),partialMapsEdges[i][k][2]])
    i += 1
  ### Sortierung der Knoten innerhalb der Kanten einfuegen *! wuerden die Kanten in edgesFromMaps nicht sortiert?
  topEdges.sort(key=takeThird, reverse=True)
  topEdges.sort(key=takeSecond)
  topEdges.sort(key=takeFirst)
  return topEdges
    
# Adjazenzmatrix des Top-Graphen
def generateTopMatrix(topVertices, topEdges):
    adj = infMatrix(len(topVertices))
    for i in range(len(topVertices)):
        adj[i][i] = 0
    for e in topEdges:
        i = elemIndex(e[0],topVertices)
        j = elemIndex(e[1],topVertices)
        adj[i][j], adj[j][i] = e[2], e[2]
    return adj

# berechnet Laenge der kuerzesten Pfade zwischen
# allen Knotenpaaren des Top-Graphen
def allPairsShortestPath(adjacencyMatrix):
    d = len(adjacencyMatrix)
    a = adjacencyMatrix
    for i in range(1,d):
            c = multiply(a,adjacencyMatrix)
            a = c
    return a

# Erzeugt Kantengewichte bei Hinzufuegung eines neuen Knotens
def generateAdjoiningEdges(vertex,partialMaps,allVertices):
    mapNr = mapKey(vertex)
    _vertex = vertexShiftDown(vertex)
    adEdges = []
    for v in allVertices[mapNr]:
        w = distance(_vertex,v,partialMaps[mapNr])
        if w > 0:
            adEdges.append([vertex,vertexShiftUp(v,mapNr),w])
    return adEdges
    
# Ergaenzt Adjazenzmatrix um Start- und Zielknoten s,t
# sowie Gewichten der Kanten zwischen s,t und dem gegeben Graphen
def adjoinEdgesToMatrix(sEdges,tEdges,adjMatrix,topVertices):
    A = infMatrix(len(adjMatrix)+2)
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix)):
            A[i][j] = adjMatrix[i][j]
    
    # Hier die verbleibenden Spalten 
    # mit den Eintraegen von s und t befuellen
    for i in range(len(sEdges)):
        index = elemIndex(sEdges[i][1],topVertices)
        A[len(A)-2][index] = sEdges[i][2]
        A[index][len(A)-2] = sEdges[i][2]
    
    for i in range(len(tEdges)):
        index = elemIndex(tEdges[i][1],topVertices)
        A[len(A)-1][index] = tEdges[i][2]
        A[index][len(A)-1] = tEdges[i][2]
        
    return A

# Gibt neue (unter) Matrix zurueck, welche "matrix" minus der 
# Zeilen und Spalten mit Indizes in "indices" ist      
def extractSubmatrix(matrix,indices):
    indices.sort()
    indices.reverse()
    for i in indices:
        del matrix[i]
    i = 0
    while i in range(len(matrix)):
        for elem in indices:
            del matrix[i][elem]
        i += 1     
    return matrix
    

#def synthPath(s,t,partialMaps,partialMapVertices,topVertices,allPairsMatrix):


########################################################################
################## Hilfsfunktionen #####################################
########################################################################

#Waehlt erstes bzw. zweites oder drittes Emelent einer Liste als key aus
def takeFirst(elem):
    return elem[0]
def takeSecond(elem):
    return elem[1]
def takeThird(elem):
    return elem[2]

# Die Teilkarten sind folgendermassen nummeriert: 
# oben links: 0, oben rechts: 1, unten links: 2, unten rechts: 3
# vertexShiftUp und vertexShiftDown regeln die Verschiebung 
# von Koordinaten innerhalb der Teilkarten in Koordinaten
# innerhalb der Gesamtkarte (Up) und zurueck (Down).

def vertexShiftUp(vertex,mapNumber):
    row = vertex[0]
    column = vertex[1]
    if mapNumber >= 2:
        row += 6
    if mapNumber % 2 != 0:
        column += 9
    return (row,column)

def vertexShiftDown(vertex):
    mapNumber = mapKey(vertex)
    if mapNumber == 0:
        return copy.deepcopy(vertex)
    row = vertex[0]
    column = vertex[1]
    if mapNumber >= 2:
        row -= 6
    if mapNumber % 2 != 0:
        column -= 9
    return (row,column)       

# Gibt index in eines Elements in einer Liste zurueck
# Gibt none zurueck, falls Element nicht in der Liste ist.    
def elemIndex(elem,elems): # adjoin edges

    for i in range(len(elems)):
        if elems[i] == elem:
            return i

# nimmt Koordinate entgegen und gibt Nr der Teilkarte zurueck
# Ausnahme: Rander und Bereich ausserhalb
def mapKey(vertex):
    a = vertex[0]
    b = vertex[1]
    if a < 1 or a == 6 or a > 11 or b < 1 or b == 9 or b > 17:
        return None
    if a < 6:
        if b < 9:
            return 0
        return 1
    if b < 9: 
        return 2
    return 3

# Gibt Distanz innerhalb einer Karte nach dem Format von PA7 an
def distance(start, end, partialMap):
  maze = copy.deepcopy(partialMap)
  if start == end:
    return 0
  q = deque([(start[0],start[1],0)])
  
  while q:
    # x - row, y - column
    x,y,d = q.popleft()
    
    for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
      if nx==end[0] and ny==end[1]:
          return d+1
      if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != "U":
        maze[nx][ny] = "U"
        q.append((nx,ny,d+1))
  
  return -1


########################################################################
################ Matrix-Operationen ####################################
########################################################################
    
def minimum(a,b):
    if a == 'inf':
        return b
    elif b == 'inf':
        return a
    else:
        return min(a,b)

def multiplyScalar(a,b):
    if a == 'inf':
        return 'inf'
    elif b == 'inf':
        return 'inf'
    else:
        return a + b 

def scalar_product(row,col):
    m = multiplyScalar(row[0],col[0])
    for i in range(1,len(col)):
        m = minimum (m, multiplyScalar(row[i],col[i]))
    return m

def get_row(A,i):
    row = []
    for j in range(len(A)):
        row.append(A[i][j])
    return row

def get_column(A,i):
    column = []
    for j in range(len(A)):
        column.append(A[j][i])
    return column

def zeroMatrix(n):
    row = []
    for i in range(n):
        row.append(0)
    mat = []
    for i in range(n):
        mat.append(copy.deepcopy(row))
    return mat

def infMatrix(n):
    row = []
    for i in range(n):
        row.append('inf')
    mat = []
    for i in range(n):
        mat.append(copy.deepcopy(row))
    return mat

def multiply(A,B):
    prod = zeroMatrix(len(A))
    for i in range(len(A)):
        col = get_column(B,i)
        for j in range(len(A)):
            prod[j][i] = scalar_product(col,get_row(A,j))
    return prod

