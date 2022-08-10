def get_classes(n,E):
    L = []
    for i in range(0, n):
        L1 = []
        for j in range(0,len(E)):
            if i == E[j][0]:
                L1.append(E[j][1])
                L1.append(E[j][0])
        if len(L1) == 0:
            L1 = [i]
        a = set(L1)
        b = list(a)
        L.append(b)
    
    return L 
    
def are_equal(list1,list2):
    if set(list1) == set(list2):
        return True
    else:
        return False
        
def are_disjoint(list1,list2):
    for i in range(0,len(list1)):
        L = list1[i]
        for k in range(0,len(list2)):
            L1 = list2[k]
            if L == L1:
                return False
    return True
    
def get_eqclasses(n,E):
    l = get_classes(n,E)
    L = []
    for i in range(0,n):
        a = l[i]
        a.sort()
        for j in range(i+1,n):
            b = l[j]
            if are_equal(a,b) == False and are_disjoint(a,b) == False:
                return L
    l.sort()
    y = -1
    for i in range(0,n):
        if len(l[i]) != 0:
            if l[i][0] != y:
                L.append(l[i])
                y = l[i][0]
    L.sort()
    return L