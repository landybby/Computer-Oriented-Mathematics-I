def eval_depth0(a):
    try:
        return(int(a))
    except ValueError:
        try:
            for i in range(len(a)):
                s = a[i]
                if s == "*":
                    return(int(a[:i])*int(a[i+1:]))
                elif s == "+":
                    return(int(a[:i])+int(a[i+1:]))
        except ValueError:
            list = []
            anfang = 0
            listop = []
            q = 1
            for i in range(len(a)):
                p = a[i]
                if p == "+":
                    list.append(int(a[anfang:i]))
                    q += 1
                    anfang = i + 1
                elif p == "*":
                    list.append(int(a[anfang:i]))
                    listop.append(q)
                    q += 1
                    anfang = i + 1
            list.append(int(a[anfang:]))
            list2 = [list[0]]
            x = 0
            if len(listop) != 0:
                for i in range(1,len(list)):
                    if i in listop:
                        list2.append(list2[-1] * list[i])
                        list2.pop(-2)
                    else:
                        list2.append(list[i])
                for i in list2:
                    x += i
            else:
                for i in list:
                    x += i
            return x
            
def evaluate(string):
    current = ""
    jack = ""
    openround = 0
    openedge = 0
    openswoosh = 0
    q = 0
    s = 0
    for o in string:
        if o == "(":
            q += 1
            openround += 1
            jack = jack + current
            current = ""
            s = 1
        elif o == "[":
            q += 1
            openedge += 1
            jack = jack + current
            current = ""
            s = 1
        elif o == "{":
            q += 1
            openswoosh += 1
            jack = jack + current
            current = ""
            s = 1
        elif o == ")":
            if openround == 0:
                raise Exception("syntaktisch inkorrekt")
            elif s == 0:
                current = current + o
                continue
            else:
                x = eval_depth0(current[1:])
                jack = jack + str(x)
                current = ""
                s = 0
                continue
        elif o == "]":
            if openedge == 0:
                raise Exception("syntaktisch inkorrekt")
            elif s == 0:
                current = current + o
                continue
            else:
                x = eval_depth0(current[1:])
                jack = jack + str(x)
                current = ""
                s = 0
                continue
        elif o == "}":
            if openswoosh == 0:
                raise Exception("syntaktisch inkorrekt")
            elif s == 0:
                current = current + o
                continue
            else:
                x = eval_depth0(current[1:])
                jack = jack + str(x)
                current = ""
                s = 0
                continue
        current = current + o
    jack = jack + current
    if q == 0:
        return(eval_depth0(string),0)
    else:
        y = evaluate(jack)
        return(y[0],y[1]+1)
        
print(evaluate("[{(1+3*(3*3+3)+1)*2}+3]"))