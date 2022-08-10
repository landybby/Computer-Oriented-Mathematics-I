def get_linedistance(points, line):
    x_i = [x[0] for x in points]
    y_i = [y[1] for y in points]
    ab_tup = line
    #a = [a_0[0] for a_0 in line]
    #b = [b_0[1] for b_0 in line]
    quad_a = 0 

    for i in range(len(x_i)):
        quad_a += (ab_tup[0] * x_i[i] + (ab_tup[1] - y_i[i])) ** 2
    return quad_a


def get_min(int_list):
    min_val = min(int_list) 
    if int_list: 
        return min_val
    else: 
        return None


def linear_regression(points, lines): 

    a = [a_0[0] for a_0 in lines]
    b = [b_0[1] for b_0 in lines]
    int_list = []

    for i in range(len(a)):
        c = get_linedistance(points,(a[i],b[i]))
        int_list.append(c)
        i += 1 
    c_min = get_min(int_list) 
    
    return c_min