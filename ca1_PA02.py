def convert_to_standard(a1, a2, b1, b2):
    f = a1
    g = b1
    a1 = min(a1, b1)
    a2 = min(a2, b2)
    b1 = max(f, g)
    b2 = max(a2, b2)
    coordinates_ab = (a1, a2, b1, b2)
    return coordinates_ab


def intersects(h, a1, a2, b1, b2):
    if a1 > 6 or a2 > h or b1 < 0 or b2 < 0:
        return False
    else:
        return True


def get_delta_x1(a1, b1):
    if min(a1, b1, 0) == 0:
        return b1 - a1
    elif max(a1, b1, 6) == 6:
        return 6 - a1
    else:
        return b1


def get_delta_x2(h, a2, b2):
    if a2 >= 0 and b2 <= h:
        return b2 - a2
    elif a2 >= 0:
        return h - a2
    elif b2 <= h:
        return b2
    else:
        return 0


def get_lattice_point_number(h, a1, a2, b1, b2):
    convert_to_standard(a1, a2, b1, b2)
    l_x1 = get_delta_x1(a1, b1)
    l_x2 = get_delta_x2(h, a2, b2)
    if h <= 0:
        return 'Die Eingabe ist fehlerhaft.'
    elif intersects(h, a1, a2, b1, b2):
        l_x1 += 1
        l_x2 += 1
        x = l_x1 * l_x2
        return 'Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt ' + str(x) + '.'
    else:
        return 'Der Schnitt der gegebenen Rechtecke ist leer.'

